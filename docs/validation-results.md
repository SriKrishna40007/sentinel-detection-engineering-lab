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

## Not demonstrated

- No Sentinel alerts were found in the SecurityAlert query for the seven-day period.
- No Sentinel incidents were observed in the reviewed incident view.
- No real RBAC assignment or mass-deletion event was found.
- End-to-end alert generation and incident creation remain unverified.

## Evidence integrity

Synthetic events are explicitly identified as query-local tests. They are not represented as real Azure events, Sentinel alerts, or incidents.

## DET-004 validation update — 2026-11-02

- Detection logic: Updated to use a rolling 10-minute self-join window rather than fixed 10-minute time buckets.
- Synthetic validation: Passed. Six synthetic successful deletion events spanning a fixed 10-minute bucket boundary were detected together (`DeletedResources = 6`).
- Real telemetry validation: The query executed successfully against `AzureActivity` for the preceding 30 minutes and returned no qualifying results.
- Sentinel configuration: Rule enabled; 5-minute frequency; 30-minute lookback; threshold greater than zero; event grouping set to one alert for all events; incident creation enabled.
- Alert/incident evidence: No real deletion-triggered Sentinel alert or incident has been demonstrated.
- Interpretation: Detection logic passed the synthetic boundary test. Real-data execution passed, but no qualifying real deletion activity was present in the validation window.
