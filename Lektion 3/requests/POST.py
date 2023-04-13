import requests
from pprint import pprint

# URL till API-endpointet för att skapa en ny användare
url = 'https://jsonplaceholder.typicode.com/users'

# Data för den nya användaren
data = {
    "name": "Ny användare",
    "username": "nyanvandare",
    "email": "nyanvandare@example.com"
}

# Skicka en POST-förfrågan till API:et med den nya datan
response = requests.post(url, json=data)

# Om förfrågan var framgångsrik (statuskod 201 Created), 
# visa den nya användardatan
if response.status_code == 201:
    new_data = response.json()
    print('Ny användare:')
    pprint(new_data, indent=4)
else:
    print('Det gick inte att skapa en ny användare.')