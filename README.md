# ARP-Attack
Arp attack to disrupt connection on blue network

# Usage
1. Update the IPS_MACS in blue_side.py to include the IPs and Mac addresses of all blue nodes. (Must be more than two blue nodes).
2. Update the IP and port for C2 in both blue_side.py and red_side.py to include the desired IP and port. 
3. Install scapy python library using pip on red node. (pip3 install scapy)
4. run python3 red_side.py on red node
6. Ensure python3 is installed on blue nodes.
7. Ensure pip3 is installed on blue nodes.
8. Install scapy python library using pip on blue nodes. (pip3 install scapy)
9. Copy blue_side.py over to the blue nodes.
10. run sudo python3 blue_side.py on blue nodes.
