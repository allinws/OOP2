import pandas as pd

# Skapa det första datasetet
df1 = pd.DataFrame({'Produkt': ['A', 'B', 'C'],
                    'Pris': [100, 200, 300]})

# Skapa det andra datasetet
df2 = pd.DataFrame({'Produkt': ['D', 'E', 'F'],
                    'Pris': [400, 500, 600]})

# Sammanfoga dataseten längs radaxeln
resultat = pd.concat([df1, df2], ignore_index=False)

print(resultat)