import requests
import requests.exceptions
from pprint import pprint

# URL till API-endpointet för att uppdatera användaren med ID 1
url = 'https://jsonplaceholder.typicode.com/users/1'

# Ny data som ska uppdatera användaren (bara uppdatera användarens email)
data = {
    'email': 'newemail@example.com'
}

# Skicka en PATCH-förfrågan till API:et med den nya datan
response = requests.patch(url, data=data)

# Om förfrågan var framgångsrik (statuskod 200), skriv ut svaret
if response.status_code == 200:
    print('Användaren har uppdaterats:')
    pprint(response.json(), indent=4)
else:
    print('Det gick inte att uppdatera användaren.')