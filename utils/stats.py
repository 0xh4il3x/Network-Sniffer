from collections import Counter
from datetime import datetime

class PacketStats:
    def __init__(self):
        self.packet_count = 0
        self.protocols = Counter()
        self.start_time = datetime.now()
    
    def update(self, packet_data):
        self.packet_count += 1
        proto = packet_data.split()[0]  # TCP/UDP/ICMP
        self.protocols[proto] += 1
    
    def get_stats(self):
        duration = (datetime.now() - self.start_time).seconds
        return {
            "total_packets": self.packet_count,
            "packets_per_second": self.packet_count / (duration or 1),
            "protocol_distribution": dict(self.protocols)
        }