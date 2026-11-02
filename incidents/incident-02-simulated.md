# Incident 02 — Potential Mass Resource Deletion

**Classification:** Simulated investigation  
**Severity:** High  
**MITRE ATT&CK:** T1485 — Data Destruction

## Scenario

One Azure identity successfully deletes more than five resources within a ten-minute window.

## Detection

Rule: DET-004 — Mass Azure Resource Deletion

The detection query groups successful DELETE operations by caller and time window.

## Investigation

1. Identify the caller and subscription.
2. Review the deleted resource IDs and operation names.
3. Establish whether the activity was part of an approved change.
4. Determine the business impact and affected services.
5. Check available backup and recovery options.

## Recommended response

- Contact the resource owner and validate the activity.
- Escalate suspected unauthorized deletion.
- Preserve Azure Activity evidence.
- Initiate approved recovery procedures if required.

## Evidence limitations

This is a simulated investigation scenario. The lab's synthetic KQL test demonstrated the query logic, but no real mass deletion or Sentinel incident was observed.
