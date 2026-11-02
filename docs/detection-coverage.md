# Detection Coverage

Microsoft Sentinel analytics rules built on Azure Activity telemetry.

| Rule | Detection objective | Severity | Validation status |
|---|---|---|---|
| DET-003 | Successful privileged role assignments | High | Query-local synthetic test passed; no matching real RBAC event observed |
| DET-004 | More than five successful resource deletions in a 10-minute window | High | Query-local synthetic test passed; no matching real deletion activity observed |
| DET-005 | Successful Azure diagnostic settings modifications | Medium | Real matching Azure Activity events observed; Sentinel alert generation not demonstrated |
| DET-006 | Five or more failed Azure operations by one caller in 15 minutes | Medium | No matching real event group observed |
| DET-007 | Repeated deployment or VM creation activity | Medium | Not independently validated with a controlled event |
| DET-008 | Network Security Group configuration changes | High | No matching real NSG activity observed |
| DET-009 | Azure Policy assignment changes | High | No matching real policy assignment modification observed |
| DET-010 | Key Vault configuration changes | High | No matching real Key Vault configuration change observed |

## Important validation notes

- Enabled analytics rules are not proof that alerts have fired.
- Synthetic datatable tests validate query logic only; they do not create Sentinel alerts.
- Real Azure Activity events were verified for diagnostic settings changes.
- No real Sentinel incidents were observed during the validation period.
- Rule scheduling and query lookback settings must be checked against the deployed rule configuration before claiming exact parity.
