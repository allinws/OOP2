import pandas as pd
import numpy as np

# Skapa en dataframe med saknade värden
data = {'name': ['Alice', 'Bob', None, 'Charlie'], 'age': [25, np.nan, 35, 40]}
df = pd.DataFrame(data)
# Innan data cleaning
print(f'{df}\n')

# Hitta saknade värden
print(f'{df.isnull()}\n')

# Ersätt saknade age-värden med medianen av 'age' och saknade namn
# med 'Unknown'.
median_age = df['age'].median()
df.fillna({'age': median_age, 'name': 'Unknown'}, inplace=True)
print(df)