#!/usr/bin/env python3
"""TCHWD-AZURE-001: auditoría y QA local en Azure Cloud Shell.
Nunca crea/modifica recursos Azure o GitHub. Sin API Antigravity no se afirma supervisión automática.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / ".tchwd-run"
FRONT = ROOT / "frontend" / "tchwd-dir"
BACK = ROOT / "backend"

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for piece in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(piece)
    return h.hexdigest()

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()

def record(name, result):
    OUT.mkdir(mode=0o700, parents=True, exist_ok=True)
    item = {"timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "expediente": "TCHWD-AZURE-001", "name": name, **result}
    with (OUT / "events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(json.dumps(item, indent=2, ensure_ascii=False))
    return item

def inspect():
    files = [ROOT / "AGENTS.md", FRONT / "package.json", FRONT / "package-lock.json",
             BACK / "app" / "main.py", BACK / "requirements.txt"]
    result = {"branch": git("branch", "--show-current"),
              "commit": git("rev-parse", "HEAD"),
              "modified": git("status", "--porcelain"),
              "files": {str(f.relative_to(ROOT)): (sha256(f) if f.is_file() else "MISSING") for f in files}}
    record("inspect", result)
    return 0 if all(f.is_file() for f in files) else 2

def run(argv, directory, name, timeout=900):
    try:
        proc = subprocess.run(argv, cwd=directory, text=True, capture_output=True,
                              timeout=timeout, check=False)
        output = (proc.stdout + "\n" + proc.stderr)[-12000:]
        return record(name, {"command": argv, "exit_code": proc.returncode, "output": output})
    except (OSError, subprocess.TimeoutExpired) as exc:
        return record(name, {"command": argv, "exit_code": -1, "error": str(exc)})

def qa():
    if git("branch", "--show-current") != "feat/tchwd-azure-manager-bootstrap":
        print("ERROR: solo rama aislada", file=sys.stderr)
        return 2
    checks = [
        (["npm", "ci", "--ignore-scripts", "--no-audit", "--no-fund"], FRONT, "npm_ci", 900),
        (["npm", "run", "test:sites"], FRONT, "frontend_tests", 400),
        (["npm", "run", "build"], FRONT, "frontend_build", 600),
    ]
    for argv, cwd, label, timeout in checks:
        output = run(argv, cwd, label, timeout)
        if output["exit_code"]:
            print("DETENIDO:", label, file=sys.stderr)
            return 1
    html = FRONT / "dist" / "client" / "index.html"
    record("build_artifact", {"exists": html.exists(), "sha256": sha256(html) if html.exists() else None})
    return 0 if html.exists() else 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["inspect", "qa"])
    parser.add_argument("--approve-local", action="store_true",
                        help="Confirma revisión humana previa de npm ci y tests locales")
    args = parser.parse_args()
    if args.action == "inspect":
        return inspect()
    if not args.approve_local:
        print("BLOQUEADO: QA requiere --approve-local tras revisar package-lock.json")
        return 2
    return qa()

if __name__ == "__main__":
    sys.exit(main())
