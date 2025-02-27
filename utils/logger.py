import datetime

def log_packet(packet_data):
    with open("output/packets.log", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {packet_data}\n")
