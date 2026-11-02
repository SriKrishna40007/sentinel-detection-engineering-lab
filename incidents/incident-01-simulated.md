# Incident 01 — Privileged Role Assignment

**Classification:** Simulated investigation  
**Severity:** High  
**MITRE ATT&CK:** T1098 — Account Manipulation

## Scenario

A privileged Azure role is assigned to an identity unexpectedly.

## Detection

Rule: DET-003 — New Privileged Role Assignment

The detection query looks for successful Azure roleAssignments/write operations.

## Investigation

1. Identify the initiating caller.
2. Review the caller IP address and timestamp.
3. Identify the target role assignment and affected scope.
4. Confirm whether the change was approved.
5. Review nearby Azure Activity events for related changes.

## Recommended response

- Validate the activity with the identity or resource owner.
- If unauthorized, follow the organization's identity incident procedure.
- Review and remove unauthorized privileges through an approved change process.
- Preserve relevant audit evidence.

## Evidence limitations

This is a simulated investigation scenario. No real privileged role assignment or Sentinel incident was observed in the lab.
