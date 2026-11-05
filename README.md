# Microsoft Sentinel Detection Engineering Lab

A practical cloud security detection engineering project built using Microsoft Azure, Microsoft Sentinel, Log Analytics and Kusto Query Language (KQL).

The project demonstrates Azure control-plane monitoring, threat detection, investigation workflows, MITRE ATT&CK mapping and evidence-driven incident analysis.

## Project Capabilities

- Azure Activity ingestion into Log Analytics.
- Eight scheduled Microsoft Sentinel analytics rules (DET-003–DET-010).
- KQL-based detection and investigation queries.
- Synthetic positive and negative detection testing.
- MITRE ATT&CK mapping with documented confidence and limitations.
- Sentinel alert-to-incident correlation.
- Incident investigation reports distinguishing simulated scenarios from real Azure evidence.

## Architecture

```text
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
SecurityAlert and SecurityIncident
       |
       v
KQL Investigation and Incident Analysis
```

See [Architecture](docs/architecture.md).

## Detection Coverage

| Rule | Detection Objective | Severity |
|---|---|---|
| DET-003 | Successful assignments of Owner, User Access Administrator and Role Based Access Control Administrator | High |
| DET-004 | More than five successful resource deletions in a rolling 10-minute window | High |
| DET-005 | Successful Azure diagnostic settings modifications | Medium |
| DET-006 | Five or more failed Azure operations by one caller in a fixed 15-minute time bucket | Medium |
| DET-007 | Five or more distinct successful non-policy ARM deployments by the same caller within a rolling 30-minute window | Medium |
| DET-008 | Successful NSG and security-rule write/delete operations | High |
| DET-009 | Successful Azure Policy assignment write/delete operations | High |
| DET-010 | Successful Key Vault write/delete operations | High |

See [Detection Coverage](docs/detection-coverage.md).

## Investigation Query Pack

Seven reusable KQL queries are included:

1. Suspicious Azure activity investigation.
2. Caller activity timeline.
3. Diagnostic settings investigation.
4. RBAC assignment investigation.
5. Network Security Group investigation.
6. Key Vault configuration investigation.
7. Sentinel alert-to-incident correlation.

The correlation query was successfully executed against the workspace. Two DET-005 alert records were correlated with two Sentinel incidents.

## MITRE ATT&CK

Documented mappings for supported detection objectives:

- DET-003: T1098.003 — Additional Cloud Roles.
- DET-005: T1685.002 — Disable or Modify Cloud Log.
- DET-008: T1686.001 — Cloud Firewall (candidate mapping).

Other detections remain deliberately unmapped where the available logic does not support a sufficiently specific technique.

See [MITRE ATT&CK Mapping](docs/mitre-attack-mapping.md).

## Incident Investigation

Three investigation reports are included:

- `incident-01-simulated.md` — simulated privileged role assignment.
- `incident-02-simulated.md` — simulated mass resource deletion.
- `incident-03-real-diagnostic-settings-change.md` — real Azure Activity and Sentinel alert/incident evidence.

The real DET-005 investigation remains open. Authorization and root cause have not been established. Both incidents relate to the same underlying event.

## Validation and Evidence Integrity

Verified results include:

- Azure Activity ingestion.
- Eight enabled scheduled analytics rules.
- Synthetic positive and negative tests for selected detection logic.
- Rolling-window detection tests.
- Real DET-005 alert generation and incident creation.
- Successful correlation of DET-005 alerts with their incidents.

Synthetic query tests are not represented as real Azure events or Sentinel alerts.

No real alert or incident generation has been demonstrated for the other detection rules.

See [Validation Results](docs/validation-results.md) and [Evidence Index](evidence/README.md).

## Repository Structure

- `rules/` — scheduled analytics rule KQL.
- `queries/` — investigation query pack.
- `tests/` — synthetic KQL validation scenarios.
- `docs/` — architecture, detection coverage, validation and ATT&CK mapping.
- `incidents/` — simulated and real incident investigation reports.
- `evidence/` — evidence index and supporting material.
- `screenshots/` — selected portal screenshots.

## Playbook Status

A functional automated Sentinel playbook has not been demonstrated in this delivery. Automation remains a potential extension after connector permissions, execution prerequisites and testing are established.

## Disclaimer

This is a learning and portfolio lab, not a production security monitoring service. Detection rules require environment-specific tuning, authorization checks and operational validation before production deployment.

No destructive Azure actions were performed as part of the documented validation.