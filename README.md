# ARP-Attack
Arp attack to disrupt connection on blue network

# Usage
1. Update the inventory.ini and IPS_MACS in blue_side.py to include the IPs and Mac addresses of all blue nodes.
2. Update the IP and port for C2 in both blue_side.py and red_side.py to include the desired IP and port
3. run python3 red_side.py on C2
4. run ansible playbook ansible-playbook start.yml -i inventory.ini
