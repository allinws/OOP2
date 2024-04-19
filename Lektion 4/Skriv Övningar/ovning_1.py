
# Ta emot ett namn från användaren
name = input("enter your name\n")

# Skapa/Öppna filen ovning_1.txt och använd den i write mode ("w")
with open("ovning_1.txt", "w") as file:
    # Skriv till filen
    file.write(name)