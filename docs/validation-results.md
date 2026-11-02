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
