
import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
df2 = pd.DataFrame({'id': [2, 3, 4], 'value': [25, 35, 45]})

merged_df = df1.merge(df2, on='id', suffixes=('_left', '_right'))

print('merged_df', merged_df)