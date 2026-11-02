# Microsoft Sentinel Detection Engineering Lab

A hands-on cloud security project demonstrating Azure Activity monitoring and Microsoft Sentinel detection engineering with Kusto Query Language (KQL).

## Project objectives

- Ingest Azure subscription activity into Log Analytics.
- Build scheduled Sentinel analytics rules for security-relevant Azure operations.
- Investigate activity using KQL.
- Map detection objectives to practical cloud security scenarios.
- Document validation results honestly, distinguishing real telemetry from synthetic query tests.

## Architecture

Azure Subscription
    |
    v
Azure Activity Diagnostic Settings
    |
    v
Log Analytics Workspace
    |
    v
AzureActivity Table
    |
    v
Microsoft Sentinel Analytics Rules
    |
    v
Potential Alerts and Incidents

See [Architecture](docs/architecture.md).

## Detection coverage

Eight scheduled analytics rules are included:

- DET-003: Privileged role assignment
- DET-004: Mass resource deletion
- DET-005: Diagnostic settings modified
- DET-006: Repeated failed Azure operations
- DET-007: Suspicious resource creation
- DET-008: Network Security Group changes
- DET-009: Policy assignment modified
- DET-010: Key Vault configuration modified

See [Detection Coverage](docs/detection-coverage.md).

## Repository structure

- `rules/` — scheduled analytics rule KQL
- `queries/` — investigation queries
- `docs/` — architecture, coverage, and validation documentation
- `incidents/` — simulated incident investigation exercises
- `evidence/` — evidence index and supporting material
- `screenshots/` — selected portal screenshots

## Validation status

Azure Activity ingestion and eight enabled analytics rules were verified. Real diagnostic settings events were observed in AzureActivity.

End-to-end Sentinel alert and incident generation has not yet been demonstrated. Synthetic query tests are query-local and are not represented as real alerts or incidents.

See [Validation Results](docs/validation-results.md).

## Disclaimer

This is a learning and portfolio lab. Detection rules require environment-specific tuning and validation before production use. No destructive Azure actions were performed as part of the documented validation.
