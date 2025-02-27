from scapy.all import IP, TCP, UDP, ICMP
from utils.geoip import get_location

def parse_packet(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        location = get_location(ip_src)  # Get geo-location of source IP
        proto = packet[IP].proto  # Protocol Number

        if packet.haslayer(TCP):
            return f"TCP Packet: {ip_src} ({location}) -> {ip_dst} | Src Port: {packet[TCP].sport}, Dst Port: {packet[TCP].dport}"
        elif packet.haslayer(UDP):
            return f"UDP Packet: {ip_src} ({location}) -> {ip_dst} | Src Port: {packet[UDP].sport}, Dst Port: {packet[UDP].dport}"
        elif packet.haslayer(ICMP):
            return f"ICMP Packet: {ip_src} ({location}) -> {ip_dst}"
        else:
            return f"IP Packet: {ip_src} ({location}) -> {ip_dst} | Protocol: {proto}"

    return "Non-IP Packet"
