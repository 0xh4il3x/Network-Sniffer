from scapy.all import sniff
from utils.pcap_export import PcapExporter
from utils.filters import get_filter
from utils.logger import log_packet
from utils.parser import parse_packet
import sys
import signal

pcap_exporter = PcapExporter()
running = True

def signal_handler(sig, frame):
    global running
    print("\nStopping Network Sniffer...")
    running = False

def packet_callback(packet):
    if not running:
        return
    parsed_data = parse_packet(packet)
    print(parsed_data)
    log_packet(parsed_data)
    pcap_exporter.write_packet(packet)

def print_banner():
    banner = """
    ╔═══════════════════════════════════╗
    ║     Network Sniffer v1.0          ║
    ║     By: Haileamlak Sahle          ║
    ╚═══════════════════════════════════╝
    """
    print(banner)

if __name__ == "__main__":
    print_banner()
    print("Starting Network Sniffer...")
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        protocol_filter = get_filter()
        # Add timeout to allow checking the running flag
        sniff(prn=packet_callback, filter=protocol_filter, store=0, stop_filter=lambda _: not running)
    except PermissionError:
        print("Error: Root privileges required!")
        print("Please run the script with sudo:")
        print("    sudo python3 sniff.py")
        sys.exit(1)
    
    print("Network Sniffer stopped successfully")
