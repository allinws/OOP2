import csv
import pandas as pd

# Read the CSV file
csv_file = "/Users/alexanderlindgren/Documents/CODE/OOP2/OOP2/Lektion 5/hemuppgift/sales_data.csv"
df = pd.read_csv(csv_file)

# Identify duplicate rows
duplicate_rows = df[df.duplicated(subset='order_id')]

# Print out duplicate rows
print("Duplicate rows found in the CSV file:")
print(duplicate_rows)