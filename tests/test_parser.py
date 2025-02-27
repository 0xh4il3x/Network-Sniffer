from utils.parser import parse_packet
from scapy.all import IP

def test_parse_packet():
    packet = IP(src="8.8.8.8", dst="192.168.1.1")
    result = parse_packet(packet)
    assert "8.8.8.8" in result
