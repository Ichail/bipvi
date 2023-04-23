from scapy.all import *
import json


def take_labeled_packets(labeled_json):
    filtered_json = []
    with open(labeled_json, 'r') as f:
        json_data = json.load(f)
    for item in json_data:
       if item['tunnel_parents   label   detailed-label'] != "-   Malicious   DDoS":
           filtered_json.append(item)
    with open('ddos.json', 'w') as f:
        json.dump(filtered_json, f, indent=1)


def time_filter_packets(pcap_filename, labeled_json):
    with open(labeled_json, 'r') as f:
        json_data = json.load(f)
        ts_set = set(str(item['ts']) for item in json_data)
    packets = rdpcap(pcap_filename)
    filtered_packets = [pkt for pkt in packets if str(pkt.time) not in ts_set]
    wrpcap('filtered.pcap', filtered_packets)


def time2_filter_packets(pcap_filename, labeled_json, labeled_type):
    with open(labeled_json, 'r') as f:
        json_data = json.load(f)
        ts_dict = {str(item['ts']): item['tunnel_parents   label   detailed-label'] for item in json_data if
                   item['tunnel_parents   label   detailed-label'] == labeled_type}
    packets = rdpcap(pcap_filename)
    filtered_packets = [pkt for pkt in packets if str(pkt.time) not in ts_dict]
    wrpcap('filtered.pcap', filtered_packets)


#time2_filter_packets("./../34-1.pcap", "./../out.json", "-   Malicious   DDoS")
take_labeled_packets("./../out.json")
# + item['tunnel_parents   label   detailed-label']
