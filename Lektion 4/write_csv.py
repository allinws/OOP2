import csv

# Skapa en lista med data som vi vill skriva till filen
data = [
    ['John', 'Åke', 'johndoe@example.com'],
    ['Pär', 'Doe', 'janedoe@example.com'],
    ['Bob', 'Smith', 'bobsmith@example.com']
]

# Öppna en CSV-fil för skrivning
with open('contacts.csv', mode='w') as file:
    # Skapa en CSV-skrivare
    writer = csv.writer(file)

    # Skriv varje rad av data till filen
    for row in data:
        writer.writerow(row)
