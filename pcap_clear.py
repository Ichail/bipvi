from scapy.all import *
from datetime import datetime


def process_packet(packet):
    pass


packets = rdpcap('34-1.pcap')
i = 0
file = open("otus.txt", "w")
for packet in packets:
    file.write(str(packet.time)+"\n")
    i += 1
