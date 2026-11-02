# Detection Coverage

Microsoft Sentinel analytics rules built on Azure Activity telemetry.

| Rule | Detection objective | Severity | Validation status |
|---|---|---|---|
| DET-003 | Successful privileged role assignments | High | Query-local synthetic test passed; no matching real RBAC event observed |
| DET-004 | More than five successful resource deletions in a rolling 10-minute window | High | Synthetic rolling-window boundary test passed; real AzureActivity query returned no qualifying events; real alert/incident not demonstrated |
| DET-005 | Successful Azure diagnostic settings modifications | Medium | Real Azure Activity event generated two Sentinel alerts and two incidents; both incidents linked to the same underlying event |
| DET-006 | Five or more failed Azure operations by one caller in 15 minutes | Medium | No matching real event group observed |
| DET-007 | Five or more distinct successful non-policy Azure Resource Manager deployments by the same caller within a rolling 30-minute window | Medium | Synthetic positive, policy-exclusion and rolling-window tests passed; real-data query returned no qualifying events; real alert/incident not demonstrated |
| DET-008 | Successful Azure Network Security Group and security-rule write/delete operations | High | Synthetic operation-filtering test passed (3 expected rows); no real networking or NSG activity observed in the checked 30-day period; real alert/incident not demonstrated |
| DET-009 | Successful Azure Policy assignment write/delete operations | High | Synthetic operation-filtering test passed (2 expected rows); no matching real policy assignment activity observed in the checked 30-day period; real alert/incident not demonstrated |
| DET-010 | Successful Key Vault write and delete operations | High | Synthetic positive/negative validation passed (2 expected rows); no matching real Key Vault activity observed in the checked 30-day period; real alert/incident not demonstrated |

## Important validation notes

- Enabled analytics rules are not proof that alerts have fired.
- Synthetic datatable tests validate query logic only; they do not create Sentinel alerts.
- Real Azure Activity events were verified for diagnostic settings changes.
- Two real Sentinel incidents were verified for DET-005; other detection rules have not yet demonstrated real alert/incident generation.
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


## DET-008 validation update — 2026-11-02

The production query detects successful NSG and nested security-rule write/delete operations. Provider matching uses substring matching, and operation filtering explicitly selects operations ending in `/WRITE` or `/DELETE`.

- Synthetic validation: Passed. Three expected records were returned: NSG write, security-rule write, and NSG delete.
- Negative cases: Unrelated VM write and failed NSG write were excluded.
- Real telemetry validation: No NSG-specific or broader Azure networking operations were found in the checked 30-day period.
- Sentinel configuration: Enabled; High severity; 5-minute frequency; 30-minute lookback; threshold greater than zero; one alert per event; incident creation enabled.
- Alert/incident evidence: No real NSG-triggered Sentinel alert or incident has been demonstrated.
- Detection limitation: The rule detects configuration modifications. It does not inspect resulting NSG rule properties to establish that a port or service became Internet-accessible.


## DET-009 validation update — 2026-11-02

The production query detects successful Azure Policy assignment write and delete operations, using provider substring matching and explicit operation suffix matching.

- Synthetic validation: Passed. Two expected records were returned: policy assignment write and policy assignment delete.
- Negative cases: Policy definition write, failed assignment write, and assignment write with an empty caller were excluded.
- Real telemetry validation: No matching Azure Policy assignment operations were found in the checked 30-day period.
- Sentinel configuration: Enabled; High severity; 5-minute frequency; 30-minute lookback; threshold greater than zero; one alert per event; incident creation enabled.
- Alert/incident evidence: No real policy-assignment-triggered Sentinel alert or incident has been demonstrated.
- MITRE ATT&CK: No technique configured because a sufficiently supported mapping was not established.

## DET-010 validation update — 2026-11-02

The production query detects successful Azure Key Vault write and delete operations. It uses provider substring matching, explicit `/WRITE` and `/DELETE` operation suffix matching, and requires a non-empty caller.

- Synthetic validation: Passed. Two expected records were returned: successful Key Vault write and successful Key Vault delete.
- Negative cases: Failed Key Vault write, unrelated Compute write, and Key Vault write with an empty caller were excluded.
- Real telemetry validation: No Key Vault operation records were found in the checked 30-day period.
- Sentinel configuration: Enabled; High severity; 5-minute frequency; 30-minute lookback; threshold greater than zero; one alert per event; incident creation enabled.
- Alert/incident evidence: No real Key Vault-triggered Sentinel alert or incident has been demonstrated.
- MITRE ATT&CK: No technique configured because a sufficiently supported mapping was not established.
- Validation limitation: Synthetic events were created in an in-memory KQL datatable. They did not create Azure resources or Sentinel alerts.
