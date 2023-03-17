import requests

url = "https://httpbin.org/delay/10"

try:
    response = requests.get(url, timeout=1)
    response.raise_for_status()
    data = response.json()
    # Gör något med data
except requests.exceptions.HTTPError as errh:
    print("HTTP error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection error:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)