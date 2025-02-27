from scapy.all import IP, TCP, UDP, ICMP

def parse_packet(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        if packet.haslayer(TCP):
            return f"TCP Packet: {ip_src} -> {ip_dst} | Src Port: {packet[TCP].sport}, Dst Port: {packet[TCP].dport}"
        elif packet.haslayer(UDP):
            return f"UDP Packet: {ip_src} -> {ip_dst} | Src Port: {packet[UDP].sport}, Dst Port: {packet[UDP].dport}"
        elif packet.haslayer(ICMP):
            return f"ICMP Packet: {ip_src} -> {ip_dst}"
        else:
            return f"IP Packet: {ip_src} -> {ip_dst} | Protocol: {proto}"
    return "Non-IP Packet"
