🚀 Network Sniffer - Python Packet Analyzer
A network sniffer built with Python that captures and analyzes network packets in real-time. Supports PCAP export, GeoIP lookup, and packet logging.

📌 Features
✅ Live Packet Capture – Sniffs network traffic using Scapy
✅ PCAP Export – Saves packets in .pcap format for Wireshark analysis
✅ GeoIP Lookup – Find the location of source IP addresses using GeoLite2
✅ Custom Packet Filtering – Capture only TCP, UDP, ICMP, or all packets
✅ Packet Logging – Saves packet details in output/packets.log


🚀 Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/network-sniffer.git
cd network-sniffer


2️⃣ Set Up a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows


3️⃣ Install Dependencies

pip install -r requirements.txt


🎯 Usage
🔹 Start Packet Sniffing

python sniff.py
📌 You'll be prompted to choose a packet filter (TCP, UDP, ICMP, or All).
📌 Packets will be logged in output/packets.log and capture.pcap.


🔹 Run the Live Dashboard

python web/app.py
Then open http://localhost:5000 in your browser to view live packets.


🛠️ Features in Detail

1️⃣ Packet Capture
The sniffer captures packets and extracts useful details:

TCP Packet: 192.168.1.10 -> 8.8.8.8 | Src Port: 53421, Dst Port: 443
UDP Packet: 192.168.1.15 -> 1.1.1.1 | Src Port: 62620, Dst Port: 53


2️⃣ PCAP Export (Wireshark)
Captured packets are saved in:

output/capture.pcap
🔹 Open this file in Wireshark for deeper analysis.


3️⃣ Live Web Dashboard
📌 Captured packets are displayed in real-time in a web browser.
💡 Uses Flask and WebSockets for instant updates.

4️⃣ GeoIP Lookup
Detects the city and country of public IP addresses:

TCP Packet: 192.168.1.10 (Addis Ababa, Ethiopia) -> 8.8.8.8 | Src Port: 53421, Dst Port: 443


5️⃣ Unit Tests
Run tests to verify functionality:
pytest tests/



📌 Dependencies
All required Python libraries are listed in requirements.txt:

scapy
flask
flask-socketio
eventlet
geoip2
pytest

Install them using:
pip install -r requirements.txt



🌎 Future Enhancements
✅ Add machine learning anomaly detection for network attacks
✅ Implement mobile notifications for suspicious activity
✅ Build a GUI-based desktop version



📜 License
This project is licensed under the MIT License.

👨‍💻 Author
📌 Haileamlak sahle
🔗 GitHub: github.com/Haileamlak1
