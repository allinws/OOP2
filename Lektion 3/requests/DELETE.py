import requests
from pprint import pprint

# URL till API-endpointet för att ta bort användaren med ID 1
url = 'https://jsonplaceholder.typicode.com/users/1'

# Skicka ett DELETE-anrop till API:et med den nya datan
response = requests.delete(url)

# Om anropet lyckas (statuskod 200), skriv ut svaret.
# Det är vanligt att API:er inte returnerar något 
# svar vid DELETE-anrop och brukar då returnera 
# statuskod 204 No Content, men jsonplaceholder
if response.status_code == 200:
    print('Användaren har tagits bort.')
else:
    print('Det gick inte att ta bort användaren.')