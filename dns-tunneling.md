# DNS Tunneling Detection

## Incident Summary
A security alert detected abnormal DNS activity from host HR-PC-22 under the account hr_assistant. The system generated a large number of DNS queries within a short period to a suspicious domain.

## Detection Details
The SIEM triggered an alert after observing 420 DNS queries to the domain aj39dk2kfj.mal-dns.net within six minutes. The domain was recently registered and contained random subdomain strings.

## Evidence

Host: HR-PC-22  
User: hr_assistant  
Process: chrome.exe  

DNS Activity:
Domain: aj39dk2kfj.mal-dns.net  
Domain Age: 2 days  
Query Count: 420 queries in 6 minutes  
Data Transferred: 180 KB  

## Analysis
The high number of DNS queries combined with randomized subdomain patterns indicates DNS tunneling. Attackers commonly use this technique to exfiltrate data or communicate with command-and-control infrastructure.

## Response / Actions Taken
- Blocked malicious domain aj39dk2kfj.mal-dns.net
- Isolated host HR-PC-22 from the network
- Escalated the incident to Level 2 security team

## Final Status
Confirmed DNS tunneling activity indicating possible data exfiltration. Host isolated and investigation escalated.
