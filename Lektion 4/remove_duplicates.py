import pandas as pd

# Skapa en dataframe med dubbletter
data = {'name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'], 'age': [25, 30, 25, 35, 30]}
df = pd.DataFrame(data)

# Innan rensning
print(f"Innan rensning: \n{df}\n")

# Ta bort dubbletter från 'name'
df.drop_duplicates(subset='name', inplace=True)
print(f"Efter rensning: \n{df}")