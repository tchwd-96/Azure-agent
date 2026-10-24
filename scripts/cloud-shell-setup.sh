#!/usr/bin/env bash
set -Eeuo pipefail
# TCHWD-AZURE-001 | Prepara exclusivamente el entorno de trabajo Cloud Shell.
cd "$(dirname "$0")/.."
printf 'Repository: %s\n' "$(pwd)"
printf 'Branch: %s\n' "$(git branch --show-current)"
printf 'Commit: %s\n' "$(git rev-parse HEAD)"
test "$(git branch --show-current)" = "feat/tchwd-azure-manager-bootstrap" || { echo "ERROR: Cambia a la rama aislada antes de continuar."; exit 2; }
command -v python3 >/dev/null
command -v node >/dev/null
command -v npm >/dev/null
python3 -m compileall -q cloud
mkdir -p .tchwd-run
chmod 700 .tchwd-run
python3 cloud/tchwd_cloud_runner.py inspect
echo "PREPARADO: sigue con python3 cloud/tchwd_cloud_runner.py qa --approve-local"
echo "NO SE HA DESPLEGADO NADA NI SE HA CREADO NINGÚN RECURSO AZURE."
