# Evidence Register

This folder tracks evidence collected during the Microsoft Sentinel lab.

## Verified evidence

| Evidence | Description | Status |
|---|---|---|
| Azure Activity ingestion | AzureActivity records successfully queried | Verified |
| DET-005 source event | One successful diagnostic-settings modification observed | Verified |
| Analytics rules | Eight scheduled analytics rules shown as enabled | Verified |
| Synthetic RBAC test | Query-local test returned expected result | Verified as simulation only |
| Synthetic deletion test | Query-local rolling-window test returned expected result | Verified as simulation only |
| DET-005 Sentinel alerts | Two alert records generated from the same underlying source event | Verified |
| DET-005 Sentinel incidents | Two incidents correlated with the two alert records; both relate to the same source event | Verified |
| Other detection rules | Real alert/incident generation not demonstrated | Not demonstrated |

## Evidence interpretation

- One source event must not be described as two independent security events.
- Two alert records and two incidents do not establish two independent security events.
- Synthetic KQL tests validate query logic only. They do not establish real Azure events or Sentinel alert generation.
- The DET-005 investigation remains open. Authorization and root cause are undetermined.

## Screenshot evidence

The following redacted screenshots should be added when available:

- Analytics rules showing the eight enabled rules.
- AzureActivity diagnostic-settings query results.
- Sentinel incidents view showing the two DET-005 incidents.

Do not publish subscription IDs, personal email addresses, caller identifiers, IP addresses, access tokens, or other sensitive operational information.
