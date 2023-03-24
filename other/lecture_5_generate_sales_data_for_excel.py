import random
import csv

# Skapa en lista med produkter och regioner
produkter = ["Produkt A", "Produkt B", "Produkt C", "Produkt D"]
regioner = ["Region 1", "Region 2", "Region 3", "Region 4"]

# Öppna en CSV-fil för att skriva data
with open("sales_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Skriv kolumnrubriker
    writer.writerow(["Datum", "Produkt", "Region", "Antal sålda", "Pris per enhet"])

    # Skriv 100 rader med slumpmässig data
    for i in range(100):
        datum = f"2022-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        produkt = random.choice(produkter)
        region = random.choice(regioner)
        antal = random.randint(10, 100)
        pris = round(random.uniform(10, 100), 2)
        writer.writerow([datum, produkt, region, antal, pris])