import os
import geoip2.database

# Define the path to the GeoLite2 database
GEOIP_DB_PATH = os.path.join(os.path.dirname(__file__), "GeoLite2-City.mmdb")

# Check if the database file exists
if not os.path.exists(GEOIP_DB_PATH):
    raise FileNotFoundError(f"GeoLite2 database not found at {GEOIP_DB_PATH}. Download it from MaxMind.")

# Load the GeoIP2 database
reader = geoip2.database.Reader(GEOIP_DB_PATH)

def get_location(ip):
    """Returns city and country for a given IP"""
    try:
        response = reader.city(ip)
        city = response.city.name
        country = response.country.name
        return f"{city}, {country}" if city else country
    except:
        return "Unknown Location"
