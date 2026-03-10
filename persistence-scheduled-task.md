# Persistence via Scheduled Task

## Incident Summary
A suspicious scheduled task was detected on host FIN-PC-07 under the user account intern_user. The task executed an encoded PowerShell command repeatedly at short intervals.

## Detection Details
SIEM generated an alert after Event ID 4698 indicated a scheduled task creation. The task executed powershell.exe with encoded parameters every 30 seconds.

## Evidence

Event ID: 4698  
User: intern_user  
Task Name: WindowsUpdateSecurity  

Task Action:
powershell.exe -nop -w hidden -enc <encoded command>

Execution Interval:
Every 30 seconds  

Network Activity:
Outbound connection to IP 102.44.12.90  

## Analysis
The scheduled task was configured to run encoded PowerShell commands repeatedly, indicating a persistence mechanism used by attackers to maintain access to the system.

## Response / Actions Taken
- Disabled and removed the malicious scheduled task
- Blocked outbound IP 102.44.12.90
- Isolated the affected host
- Escalated the incident to Level 2 security team

## Final Status
Confirmed persistence mechanism established through scheduled task. Incident escalated for further investigation.
