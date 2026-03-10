# Brute Force Attack Investigation

## Incident Summary
A security alert was triggered after multiple failed login attempts were detected against the Administrator account on host WIN-SEC-01. The activity originated from external IP address 185.220.101.15 within a short time window.

## Detection Details
The SIEM generated an alert after observing repeated authentication failures. Event ID 4625 occurred 48 times within two minutes. Shortly afterward, Event ID 4624 recorded a successful login from the same source IP using Remote Desktop Protocol (Logon Type 10).

## Evidence

Event ID: 4625  
Account: Administrator  
Source IP: 185.220.101.15  
Attempts: 48 failed logins in 2 minutes  

Event ID: 4624  
Account: Administrator  
Logon Type: 10 (Remote Desktop)  
Source IP: 185.220.101.15  
Status: Successful login  

## Analysis
The high number of failed login attempts followed by a successful authentication from the same IP address strongly indicates a brute force password guessing attack. The attacker likely discovered the correct password and gained remote access to the system.

## Actions Taken
- Blocked source IP 185.220.101.15 at the firewall
- Isolated affected host from the network
- Escalated incident to Level 2 security team for deeper investigation

## Final Status
Confirmed brute force attack with successful account compromise. Incident contained and escalated for remediation.
