import pandas as pd

# create two sample dataframes
df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
df2 = pd.DataFrame({'id': [2, 3, 4], 'value': [25, 35, 45], 'category': ['A', 'B', 'C']})

# merge on 'id' column with an outer join
merged_df = df1.merge(df2, on='id', how='outer')

# join based on index with a left join
joined_df = df1.join(df2.set_index('id'), rsuffix='_right')

print("Merged DataFrame:\n", merged_df)
print("\nJoined DataFrame:\n", joined_df)