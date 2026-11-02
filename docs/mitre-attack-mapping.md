# MITRE ATT&CK Mapping

Framework: MITRE ATT&CK Enterprise
Review date: 2026-11-02

## Mapping principles

Mappings represent adversary behaviors that a detection could help identify.
A matching Azure operation does not prove malicious intent or establish that
the full ATT&CK technique occurred.

Only sufficiently supported mappings are assigned. Other detections remain
unmapped until their logic or telemetry provides stronger behavioral evidence.

## Supported mappings

| Rule | Technique | Tactic | Mapping rationale | Confidence / limitation |
|---|---|---|---|---|
| DET-003 | T1098.003 - Additional Cloud Roles | Persistence, Privilege Escalation | Successful Azure role assignments can grant additional cloud roles or permissions. | Moderate. The rule detects role assignment writes but does not establish that the assignment was unauthorized or adversary-controlled. |
| DET-005 | T1685.002 - Disable or Modify Cloud Log | Defense Impairment | Diagnostic-settings modifications can alter cloud logging collection and integrations. | Moderate. The rule detects diagnostic-settings writes; it does not inspect before/after configuration to prove logging was disabled or reduced. |
| DET-008 | T1686.001 - Cloud Firewall | Defense Impairment | Azure NSG and nested security-rule modifications can weaken cloud network access controls. | Candidate. The current rule detects writes/deletes but does not inspect rule properties to establish widened access or weakened restrictions. |

## Deliberately unmapped detections

| Rule | Reason |
|---|---|
| DET-004 | Resource deletion alone does not establish data destruction or another specific adversary technique. |
| DET-006 | Failed Azure operations by one caller do not establish a specific adversary behavior. |
| DET-007 | Repeated ARM deployments are broad administrative activity; the current rule does not identify a specific malicious deployment behavior. |
| DET-009 | Policy assignment changes may weaken governance, but the current query does not establish a specific ATT&CK technique. |
| DET-010 | Key Vault configuration changes alone do not establish credential theft, secret access, or a specific adversary technique. |

## Mapping limitations

- ATT&CK mappings describe potential adversary behavior, not proof of compromise.
- DET-005 and DET-008 require configuration-diff or resulting-state analysis for stronger behavioral confidence.
- Detection rules should be reviewed when their query logic or ATT&CK taxonomy changes.
- Unmapped is preferable to an unsupported technique assignment.

## References

- T1098.003 - Additional Cloud Roles:
  https://attack.mitre.org/techniques/T1098/003/
- T1685.002 - Disable or Modify Cloud Log:
  https://attack.mitre.org/techniques/T1685/002/
- T1686.001 - Cloud Firewall:
  https://attack.mitre.org/techniques/T1686/001/
