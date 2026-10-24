# Codex instructions — TCHWD Azure Manager

## Scope
Work only inside this repository and the authorized development branch. Build an Azure administration dashboard and read-only FastAPI backend. No production modifications, resource creation, deployments, billing changes, or external communications.

## Governance
- Dirección General (@tchwd-dir) has final approval authority.
- ld-dev is the proposed technical owner.
- Follow SEC-001: least privilege, do not persist secrets, avoid sensitive information in logs, encrypt controlled stored data where feasible, and keep keys separate.
- Follow WIP-005: at most five globally active TCHWD tasks; do not assume available capacity or activate tasks automatically.
- Keep Programados updates as proposals only until explicitly authorized.
- Mark predictive recommendations with (prog).

## Engineering rules
- Python FastAPI; strict typing; small tested units; dependency pinning after review.
- Azure authentication: prefer DefaultAzureCredential, managed identities and RBAC Reader scoped minimally.
- Read-only allowlist of Azure API operations.
- Never request Owner/Contributor roles, store raw access tokens, or emit secret values.
- Do not use terraform apply, az deployment, az resource create/delete/update, or other modifying operations.
- Test with mocks before real Azure reads.
- No external services or paid OpenAI API calls without explicit approval.
- Document assumptions, test evidence and costs. Never claim unrun tests passed.

## Acceptance
- Documented access model, threat notes, API contracts and read-only endpoint tests.
- Explicit zero-deployment posture until Dirección authorizes a later phase.
