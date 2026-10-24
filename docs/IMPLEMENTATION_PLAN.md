# TCHWD-AZURE-001 · Implementation plan v0.1

Status: proposed / isolated development. No Azure connection, deployment or paid API operation is authorized by this file.

## Phase 0: verified bootstrap
- README initialized on main and work prepared in isolated branch.
- No secrets, production changes, or deployment.

## Phase 1: read-only foundation
- Review Azure subscription and tenant IDs through safe CLI reads.
- Identify least-privilege RBAC scope; approve access separately.
- Implement FastAPI health endpoint and mock-first tests.
- Add Azure Resource Graph inventory and Cost Management read integrations only after service availability/permissions reviewed.

## Phase 2: dashboard
- Build responsive overview for subscriptions, resource groups, usage and monitoring.
- Record source timestamps and partial permission errors.
- Ensure UI does not expose mutating operations.

## Phase 3: validation
- Unit and integration tests with fixtures and mocked Azure clients.
- SEC-001 review; audit of secrets and dependency safety.
- WIP-005 / Programados reconciliation plan.
- Cost and deployment forecast for separate Dirección approval.

## Acceptance gates
1. No modified Azure resources.
2. No secrets in Git/history/logs.
3. Read-only API and RBAC scope documented.
4. No deployments or paid infrastructure created.
5. No direct commits to main beyond initial README without new approval.
