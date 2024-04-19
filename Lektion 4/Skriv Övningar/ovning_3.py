import csv

# Skapa en lista med data som vi vill skriva till filen
data = [
    ["namn","ålder","stad"],
    ["Alice","25","Stockholm"],
    ["Bob","30","Göteborg"],
]

# Öppna en CSV-fil för skrivning
with open('people.csv', mode='w') as file:
    # Skapa en CSV-skrivare
    writer = csv.writer(file)
        
    # Skriv varje rad av data till filen
    for row in data:
        writer.writerow(row)