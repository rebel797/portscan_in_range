import socket
from IPy import IP
def scan_port(ipaddress , port) :
   try:
      sock = socket.socket()
      sock.settimeout(0.5)
      sock.connect((ipsddress , port))
      print("[+]port" +str(port)+"is open")
   except:
      print("[+]port" + str(port)+"is closed")
ipaddress = input("[+]enter target to scan:")
for port in range(1,10):
   scan_port(ipaddress,port)
    
    