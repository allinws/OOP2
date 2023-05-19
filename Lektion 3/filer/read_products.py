import csv
import os

path = os.path.join(os.path.dirname(__file__), 'product_list.csv')

with open(path, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Det första elementet i listan är rubrikerna följt av produkterna
print(data[0])
for product in data[1:]:
    print(product)

# Därför är antalet produkter längden på listan minus 1
count_products = len(data) - 1
print(f"Count products: {count_products}")
