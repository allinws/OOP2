import pandas as pd

# Skapa en dataframe med inkonsekventa datum
data = {'date': ['1/1/2022', '2022-01-02', '2022.01.03']}
df = pd.DataFrame(data)
# Innan konvertering av datum
print(f'{df}\n')

# Konvertera datum till enhetligt format
df['date'] = pd.to_datetime(df['date'])
print(df)