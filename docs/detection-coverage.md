# Detection Coverage

Microsoft Sentinel analytics rules built on Azure Activity telemetry.

| Rule | Detection objective | Severity | Validation status |
|---|---|---|---|
| DET-003 | Successful privileged role assignments | High | Query-local synthetic test passed; no matching real RBAC event observed |
| DET-004 | More than five successful resource deletions in a rolling 10-minute window | High | Synthetic rolling-window boundary test passed; real AzureActivity query returned no qualifying events; real alert/incident not demonstrated |
| DET-005 | Successful Azure diagnostic settings modifications | Medium | Real matching Azure Activity events observed; Sentinel alert generation not demonstrated |
| DET-006 | Five or more failed Azure operations by one caller in 15 minutes | Medium | No matching real event group observed |
| DET-007 | Five or more distinct successful non-policy Azure Resource Manager deployments by the same caller within a rolling 30-minute window | Medium | Synthetic positive, policy-exclusion and rolling-window tests passed; real-data query returned no qualifying events; real alert/incident not demonstrated |
| DET-008 | Network Security Group configuration changes | High | No matching real NSG activity observed |
| DET-009 | Azure Policy assignment changes | High | No matching real policy assignment modification observed |
| DET-010 | Key Vault configuration changes | High | No matching real Key Vault configuration change observed |

## Important validation notes

- Enabled analytics rules are not proof that alerts have fired.
- Synthetic datatable tests validate query logic only; they do not create Sentinel alerts.
- Real Azure Activity events were verified for diagnostic settings changes.
- No real Sentinel incidents were observed during the validation period.
- Rule scheduling and query lookback settings must be checked against the deployed rule configuration before claiming exact parity.

## DET-004 validation update — 2026-11-02

The fixed-bucket implementation was replaced with a rolling 10-minute self-join query. A synthetic test containing six successful deletion events across a fixed bucket boundary returned the expected result (`DeletedResources = 6`). The query was also executed against real `AzureActivity` data for the preceding 30 minutes and returned no qualifying events. The rule is enabled with a 5-minute frequency, 30-minute lookback, single-alert event grouping, and incident creation enabled. A real deletion-triggered Sentinel alert and incident have not been demonstrated.

## DET-007 validation update — 2026-11-02

The original resource-creation objective was replaced with detection of repeated successful non-policy Azure Resource Manager deployment activity. The query extracts the deployment entity from `Properties.entity`, excludes Azure Policy remediation deployments, and correlates distinct deployment entities by caller and subscription over a rolling 30-minute window.

- Synthetic positive validation: Passed. Five distinct deployments by the same caller and subscription met the detection threshold.
- Policy exclusion validation: Passed. A synthetic `PolicyDeployment_` record was excluded.
- Synthetic rolling-window validation: Passed. Five events spanning 10:28–10:32 were detected together across the 10:30 clock boundary.
- Real telemetry validation: The production query executed against real `AzureActivity` data and returned no qualifying non-policy deployments in the checked period.
- Sentinel configuration: Rule enabled; Medium severity; 5-minute frequency; 30-minute lookback; threshold greater than zero; single-alert event grouping; incident creation enabled.
- Alert/incident evidence: No real deployment-triggered Sentinel alert or incident has been demonstrated.
- MITRE ATT&CK: No technique configured because a sufficiently supported mapping was not established.
