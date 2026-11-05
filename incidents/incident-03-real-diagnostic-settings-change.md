# Incident 03 — Real Azure Diagnostic Settings Modification

## Classification

- Evidence type: Real Azure Activity telemetry and Microsoft Sentinel alert/incident records
- Detection rule: DET-005 - Azure Diagnostic Settings Modified
- Severity: Medium
- Incident status at evidence collection: New
- Investigation status: Partially investigated
- Authorization: Pending confirmation
- Root cause: Undetermined

## Executive Summary

On 31 October 2026 at 15:46:14 UTC, Azure Activity recorded a successful subscription-level diagnostic settings write operation.

The deployed Microsoft Sentinel analytics rule DET-005 matched the event and generated a full alert. Two Sentinel incidents were subsequently created from alerts associated with the same underlying Azure Activity event.

The available evidence confirms the event and detection pipeline. It does not establish whether the change was authorized or malicious.

## Source Event Evidence

| Field | Observed value |
|---|---|
| Event time (UTC) | 2026-10-31 15:46:14 |
| Operation | MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE |
| Activity status | Success |
| Status code | OK |
| Event category | Administrative |
| Caller object ID | Redacted |
| Caller IP | Redacted |
| Resource name | subscriptionToLa |
| Resource provider | MICROSOFT.INSIGHTS |
| Scope | Subscription-level diagnostic setting |
| Event data ID | Redacted |

Resource entity:

`/subscriptions/{subscription-id}/providers/Microsoft.Insights/diagnosticSettings/subscriptionToLa`

Source identifiers have been redacted from this public report.

## Detection Evidence

- Analytics rule: DET-005 - Azure Diagnostic Settings Modified
- Rule ID: Redacted
- Severity: Medium
- Query result count: 1 for each recorded rule execution
- Alert generation status: Full alert created
- Sentinel processing: True
- Event grouping: AlertPerEvent
- Data source: law-sentinel-detection-lab

The original detection query matched successful `MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE` operations.

## Incident Evidence

Two incidents were observed:

| Incident | Alert ID | Severity | Status |
|---|---|---|---|
| 1 | Redacted | Medium | New |
| 2 | Redacted | Medium | New |

Both incidents have the title:

`DET-005 - Azure Diagnostic Settings Modified`

Both refer to the same underlying event timestamp. The available evidence therefore indicates duplicate alert/incident generation for one event, not two independently verified diagnostic-setting modifications.

## Investigation and Assessment

### Confirmed

1. Azure Activity recorded a successful diagnostic settings write.
2. The operation targeted a subscription-level diagnostic setting.
3. The event included caller identity and source network metadata.
4. DET-005 matched the event.
5. Sentinel generated alerts and created two incidents.

### Not yet confirmed

1. Whether the caller was authorized to make the change.
2. Whether the operation was part of the lab's planned diagnostic settings configuration.
3. Whether the resulting diagnostic settings weakened, strengthened, or otherwise changed monitoring coverage.
4. Why two incidents were created for the same underlying event.

### Preliminary risk

Changes to subscription-level diagnostic settings can affect audit and security monitoring visibility. The operation warrants investigation.

However, a successful administrative operation is not by itself evidence of malicious activity. No malicious classification is made in this report.

## Recommended Investigation Actions

1. Resolve the caller identity using authorized administrative access.
2. Confirm with the subscription administrator whether the change was planned and approved.
3. Review the diagnostic setting configuration before and after the event, if historical configuration evidence is available.
4. Confirm that required Azure Activity categories continued to be sent to the intended Log Analytics workspace.
5. Review the two incidents and determine whether duplicate handling or correlation is appropriate.
6. Record the authorization decision and investigation outcome before closing either incident.

## Outcome

Status: Open — investigation incomplete.

This report documents a real Azure Activity event and its corresponding Sentinel detection and incident records. Authorization, intent, root cause, and final disposition remain unverified.

No claim of malicious activity, confirmed compromise, or incident closure is made.
