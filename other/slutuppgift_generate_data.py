import csv
import random
from datetime import date, timedelta

def generate_sales_data(num_rows):
    product_ids = range(1, 11)
    product_names = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G', 'Product H', 'Product I', 'Product J']
    regions = ['North', 'South', 'East', 'West']

    sales_data = []

    for _ in range(num_rows):
        product_index = random.randint(0, len(product_ids) - 1)
        region = random.choice(regions)
        unit_price = round(random.uniform(10, 100), 2)
        quantity = random.randint(1, 20)
        sale_date = date.today() - timedelta(days=random.randint(1, 365))

        sales_data.append({
            'date': sale_date,
            'product_id': product_ids[product_index],
            'product_name': product_names[product_index],
            'region': region,
            'unit_price': unit_price,
            'quantity': quantity,
        })

    return sales_data

def write_sales_data_to_csv(sales_data, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['date', 'product_id', 'product_name', 'region', 'unit_price', 'quantity',]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in sales_data:
            writer.writerow(row)

if __name__ == '__main__':
    num_rows = 1000
    file_name = 'sales_data.csv'

    sales_data = generate_sales_data(num_rows)
    write_sales_data_to_csv(sales_data, file_name)
    print(f"Generated {num_rows} rows of sales data and saved it to {file_name}.")