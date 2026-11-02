# Architecture

## Overview

This project demonstrates Microsoft Sentinel detection engineering using Azure Activity telemetry collected in a Log Analytics workspace.

## Data flow

1. Azure subscription generates control-plane activity events.
2. Azure Activity diagnostic settings route activity logs to Log Analytics.
3. Microsoft Sentinel uses the Log Analytics workspace as its data source.
4. Scheduled analytics rules evaluate KQL queries against AzureActivity.
5. Matching events can generate alerts and incidents, depending on rule configuration.

## Components

- Azure subscription
- Azure Activity diagnostic settings
- Log Analytics workspace
- AzureActivity table
- Microsoft Sentinel
- Scheduled analytics rules
- KQL investigation queries

## Scope

This lab focuses on Azure control-plane security monitoring. It does not claim endpoint detection, network packet inspection, or automated incident response.
