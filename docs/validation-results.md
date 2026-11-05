# Validation Results

## Environment

- Microsoft Sentinel workspace: law-sentinel-detection-lab
- Log Analytics table: AzureActivity
- Validation window: 31 October–2 November 2026

## Verified

- Azure Activity ingestion was observed.
- Eight scheduled analytics rules were created and enabled.
- Diagnostic settings write events were found in AzureActivity.
- Synthetic query tests returned expected results for selected RBAC and mass-deletion detection logic.
- DET-004 rolling-window synthetic boundary test passed with six deletion events.
- DET-007 synthetic positive test passed with five distinct deployments.
- DET-007 synthetic PolicyDeployment exclusion test passed.
- DET-007 synthetic rolling-window boundary test passed with five deployments across 10:30.

## Not demonstrated

- DET-005 generated two real Sentinel alerts and two incidents from the same underlying diagnostic-settings write event; these are not two distinct changes.
- No real RBAC assignment or mass-deletion event was found.
- No qualifying real non-policy deployment activity was returned by the DET-007 production query.
- End-to-end alert generation and incident creation were demonstrated for DET-005. They have not been demonstrated for the other detection rules.

## DET-004 validation

- Detection logic: Rolling 10-minute self-join window.
- Synthetic validation: Passed. Six synthetic successful deletion events spanning a fixed 10-minute bucket boundary were detected together (`DeletedResources = 6`).
- Real telemetry validation: Query executed against AzureActivity for the preceding 30 minutes and returned no qualifying results.
- Sentinel configuration: Enabled; 5-minute frequency; 30-minute lookback; threshold greater than zero; single-alert event grouping; incident creation enabled.
- Alert/incident evidence: No real deletion-triggered Sentinel alert or incident has been demonstrated.

## DET-007 validation

- Detection logic: Five or more distinct successful non-policy Azure Resource Manager deployments by the same caller within a rolling 30-minute window.
- Deployment identity: Extracted from `Properties.entity`.
- Policy exclusion: Deployment entities containing `PolicyDeployment_` are excluded.
- Synthetic positive validation: Passed. Five distinct deployments met the threshold.
- Synthetic exclusion validation: Passed. The synthetic PolicyDeployment record was excluded.
- Synthetic rolling-window validation: Passed. Five deployments from 10:28 through 10:32 were detected together across the 10:30 clock boundary.
- Real telemetry validation: Production query executed against real AzureActivity data and returned no qualifying non-policy deployments in the checked period.
- Sentinel configuration: Enabled; Medium severity; 5-minute frequency; 30-minute lookback; threshold greater than zero; single-alert event grouping; incident creation enabled.
- MITRE ATT&CK: No technique configured because a sufficiently supported mapping was not established.
- Alert/incident evidence: No real deployment-triggered Sentinel alert or incident has been demonstrated.

## Evidence integrity

Synthetic events are explicitly identified as query-local tests. They are not represented as real Azure events, Sentinel alerts, or incidents.

A successful query execution is not equivalent to a generated Sentinel alert. An enabled analytics rule is not proof of detection in production.

## DET-008 validation

- Detection logic: Successful Azure Network Security Group and nested security-rule write/delete operations.
- Synthetic validation: Passed. Three expected records were returned: NSG write, security-rule write, and NSG delete.
- Negative validation: Unrelated VM write and failed NSG write were excluded.
- Real telemetry validation: No NSG-specific or broader Azure networking operations were found in the checked 30-day period.
- Sentinel configuration: Enabled; High severity; 5-minute frequency; 30-minute lookback; threshold greater than zero; one alert per event; incident creation enabled.
- Alert/incident evidence: No real NSG-triggered Sentinel alert or incident has been demonstrated.
- Detection limitation: The rule detects configuration modifications. It does not inspect resulting NSG rule properties to establish Internet exposure.

## DET-009 validation

- Detection logic: Successful Azure Policy assignment write and delete operations.
- Synthetic validation: Passed. Two expected records were returned: policy assignment write and policy assignment delete.
- Negative validation: Policy definition write, failed assignment write, and assignment write with an empty caller were excluded.
- Real telemetry validation: No matching Azure Policy assignment operations were found in the checked 30-day period.
- Sentinel configuration: Enabled; High severity; 5-minute frequency; 30-minute lookback; threshold greater than zero; one alert per event; incident creation enabled.
- MITRE ATT&CK: No technique configured because a sufficiently supported mapping was not established.
- Alert/incident evidence: No real policy-assignment-triggered Sentinel alert or incident has been demonstrated.

## DET-010 validation

- Detection logic: Successful Azure Key Vault write and delete operations.
- Synthetic validation: Passed. Two expected records were returned: successful Key Vault write and successful Key Vault delete.
- Negative validation: Failed Key Vault write, unrelated Compute write, and Key Vault write with an empty caller were excluded.
- Real telemetry validation: No matching Key Vault operations were found in the checked 30-day period.
- Sentinel configuration: Enabled; High severity; 5-minute frequency; 30-minute lookback; threshold greater than zero; one alert per event; incident creation enabled.
- MITRE ATT&CK: No technique configured because a sufficiently supported mapping was not established.
- Alert/incident evidence: No real Key Vault-triggered Sentinel alert or incident has been demonstrated.
- Validation limitation: Synthetic events were evaluated in an in-memory KQL datatable. They did not create Azure resources or Sentinel alerts.

## Investigation query pack validation — 2026-11-02

- Seven KQL investigation queries created under `queries/`.
- Sentinel alert/incident correlation query executed successfully against `SecurityAlert` and `SecurityIncident`.
- Schema validation confirmed `SecurityAlert.SystemAlertId` and `SecurityIncident.AlertIds`.
- Two DET-005 alert records were correlated with Sentinel incidents #1 and #2.
- Both incidents are Medium severity and currently New.
- Both records relate to the same underlying diagnostic-settings modification; they are not two distinct security events.
- Investigation status: Authorization and root cause remain undetermined.


## Final repository validation scope

DET-003 synthetic validation returned the three expected built-in privileged
roles and excluded the negative cases. The live query executed without error
and returned no matching event in the selected time range.

Repository CI performs static file, rule inventory and evidence-reference
checks. Runtime KQL validation remains dependent on execution in Microsoft
Sentinel. No claim is made that every rule generated a real alert or incident.
