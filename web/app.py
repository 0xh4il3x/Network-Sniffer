from flask import Flask, render_template
from flask_socketio import SocketIO
from scapy.all import sniff

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

@app.route("/")
def index():
    return render_template("index.html")

def packet_callback(packet):
    packet_info = f"{packet.summary()}"
    socketio.emit('new_packet', {'data': packet_info})

def start_sniffing():
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    socketio.start_background_task(start_sniffing)
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
