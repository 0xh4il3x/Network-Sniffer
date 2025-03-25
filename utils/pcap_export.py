from scapy.utils import PcapWriter

class PcapExporter:
    def __init__(self, filename="output/capture.pcap"):
        self.pcap_writer = PcapWriter(filename, append=True, sync=True)

    def write_packet(self, packet):
        self.pcap_writer.write(packet)
