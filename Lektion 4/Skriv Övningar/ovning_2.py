import json

# skapa en dict
data = {
  "namn": "Alice",
  "ålder": 25,
  "stad": "Stockholm"
}

# Skapa/Öppna filen ovning_2.txt och använd den i write mode ("w")
with open("ovning_2.json", "w") as file:
    # använd json module för att skriva in data till filen
    json.dump(data, file, indent=4)