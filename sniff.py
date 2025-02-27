from scapy.all import sniff
from utils.filters import get_filter
from utils.logger import log_packet
from utils.parser import parse_packet

def packet_callback(packet):
    parsed_data = parse_packet(packet)
    print(parsed_data)
    log_packet(parsed_data)

if __name__ == "__main__":
    print("Starting Network Sniffer...")
    protocol_filter = get_filter()
    sniff(prn=packet_callback, filter=protocol_filter, store=0)
