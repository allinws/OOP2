import pandas as pd

# Skapa en dataframe med outliers
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 150]}
df = pd.DataFrame(data)
# Innan data cleaning
print(f'{df}\n')

# Ta bort outliers från 'age'
df['age'] = df['age'].clip(lower=0, upper=100)
print(df)