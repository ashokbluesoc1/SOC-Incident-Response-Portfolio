# Webshell Upload and Execution Investigation

## Incident Summary
A security alert detected suspicious activity on a web server involving file upload and execution. A malicious file disguised as an image was uploaded and later executed through the web application.

## Detection Details
Web server logs recorded a POST request uploading a file named invoice.jpg.php to the server using upload.php. Shortly after, a GET request executed the uploaded file from the uploads directory.

## Evidence

Log Source: Apache Web Server Logs  
Host: WebServer-01  

HTTP Requests:
POST /upload.php  
Filename: invoice.jpg.php  

GET /uploads/invoice.jpg.php  
Status: 200 (Execution Successful)

Process Chain:
apache.exe → php.exe → cmd.exe → powershell.exe  

Network Activity:
Outbound connection to IP 45.89.33.120  
Port: 8080  

## Analysis
The uploaded file contained executable PHP code disguised as an image file. Once executed, the webshell allowed the attacker to run system commands through the web server and establish communication with an external system.

## Response / Actions Taken
- Isolated the affected web server from the network
- Removed the malicious webshell file from the uploads directory
- Blocked attacker IP 45.89.33.120
- Escalated the incident to the Level 2 security team

## Final Status
Confirmed webshell compromise on the web server. Malicious file removed and investigation escalated.
