import requests

def get_location(ip):
    """Uses free IP-API for lightweight IP geolocation"""
    try:
        if ip.startswith('192.168.') or ip.startswith('10.') or ip.startswith('172.'):
            return 'Local Network'
        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=2)
        data = response.json()
        if data['status'] == 'success':
            return f"{data['city']}, {data['country']}"
        return "Unknown"
    except:
        return "Unknown"
