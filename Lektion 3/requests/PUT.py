import requests
from pprint import pprint

# URL till API-endpointet för att uppdatera en användare med ID 1
url = 'https://jsonplaceholder.typicode.com/users/1'

# Ny data för användaren
data = {
    "name": "Ny användare",
    "username": "nyanvandare",
    "email": "nyanvandare@example.com"
}

# Skicka en PUT-förfrågan till API:et med den nya datan
response = requests.put(url, json=data)

# Om förfrågan var framgångsrik (statuskod 200), visa den uppdaterade datan
if response.status_code == 200:
    updated_data = response.json()
    print('Uppdaterad data:')
    pprint(updated_data, indent=4)
else:
    print('Det gick inte att uppdatera användaren.')