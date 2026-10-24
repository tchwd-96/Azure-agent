# TCHWD-DIR v0.1 · Integration manifest

Source: user-authorized archive `TCHWD-DIR_v0.1_prototipo(1).zip`.
Target branch: `feat/tchwd-azure-manager-bootstrap`.
Target folder: `frontend/tchwd-dir/`, preserving all original files and relative paths.
Integration relationship: addition of an isolated React/Vite prototype, **not** a replacement for Azure Manager, Programados or WIP-005.

## Scope
- Original prototype: 15 files, React 19.2 and Vite 6.4.
- Keep the original `frontend/tchwd-dir/README.md` and `frontend/tchwd-dir/AGENTS.md` separate from the repository root policies.
- `frontend/tchwd-dir/.openai/hosting.json` and Sites worker are legacy prototype packaging; not Azure deployment configuration.
- Prototype data are DEMO. No auth, persistence, backend integration or production-ready WIP-005.
- No deploy, merge, resource creation, financial operation or change to production is permitted without new authorization.

## Validation after uploading source
1. `cd frontend/tchwd-dir && npm ci`
2. `npm run build`
3. `npm run test:sites`
4. Review `design-qa.md` and test mobile viewport.
5. Evaluate a separate Azure-friendly Vite build process; do not assume the Sites worker works in App Service F1.
6. Audit dependencies and secrets before deployment.

## Status
Integration instructions committed. Original source files must be committed separately before marking the import complete. Do not claim this manifest alone implements the frontend.
