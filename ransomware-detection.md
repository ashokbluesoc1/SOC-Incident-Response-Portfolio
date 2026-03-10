# Ransomware Activity Detection

## Incident Summary
A security alert detected suspicious PowerShell activity on host Sales-PC-14 under the account sales_user. The system executed a command to delete shadow copies and began renaming multiple files within a short period.

## Detection Details
The SIEM triggered an alert after identifying the execution of the command "vssadmin delete shadows /all /quiet" through PowerShell. Shortly after, the system recorded 80 file renaming events and abnormal SMB connections to multiple internal hosts.

## Evidence

Host: Sales-PC-14  
User: sales_user  
Process: powershell.exe  

Command Executed:
vssadmin delete shadows /all /quiet  

Indicators:
• 80 files renamed to .locked extension  
• SMB (port 445) connections to 10 internal hosts  
• Outbound connection to external IP 62.113.114.90  

## Analysis
The deletion of shadow copies combined with rapid file encryption and propagation attempts via SMB strongly indicates ransomware activity. The attacker attempted to encrypt files and spread the malware to other systems within the network.

## Actions Taken
- Immediately isolated the affected host from the network
- Blocked outbound connection to IP 62.113.114.90
- Disabled SMB communication to prevent lateral spread
- Escalated the incident to Level 2 incident response team

## final status 
confirmed Ransomwsre activity. host isolated and incident escalated for full 
malware containment and recovery procedures 
