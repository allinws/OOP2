import csv
import random
from datetime import datetime, timedelta

# Helper functions


def random_price():
    return round(random.uniform(10, 500), 2)

def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def random_index(last_index):
    return random.randint(0, last_index)

# Define product and customer data
products = ['T-shirt', 'Jeans', 'Sneakers', 'Jacket', 'Watch']
customers = [
    'john@example.com',
    'jane@example.com',
    'bob@example.com',
    'johndoe1234@example.com',
    'sarahjones5678@gmail.com',
    'brianwilson4321@hotmail.com',
    'katewilliams7890@outlook.com',
    'davidlee2468@yahoo.com',
    'laurensmith1357@gmail.com',
    'adamjohnson2468@yahoo.com',
    'amybrown7890@outlook.com',
    'jenniferwhite1234@gmail.com',
    'matthewjackson5678@hotmail.com',
    'chrisgreen2468@outlook.com',
    'rachelgray7890@yahoo.com',
    'ericmorris1234@example.com',
    'stephaniebrown5678@gmail.com',
    'nickjones2468@outlook.com',
    'laurawilson7890@example.com',
    'patricktaylor1357@yahoo.com',
    'jessicasmith5678@gmail.com',
    'andrewbrown2468@outlook.com',
    'emilydavis7890@example.com',
]

# Define order count and date range
order_count = 1000
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 3, 17)

# Generate sales dataset
orders = []
for i in range(order_count):
    order_date = random_date(start_date, end_date)
    order_id = i + 1
    customer_email = random.choice(customers)
    product_count = random.randint(1, 5)
    product_list = random.sample(products, product_count)
    total_price = sum(random_price() for _ in range(product_count))
    order = {
        'order_id': order_id,
        'customer_email': customer_email,
        'product_list': ', '.join(product_list),
        'total_price': total_price,
        'order_date': order_date.strftime('%m/%d/%Y %H:%M:%S')
    }
    orders.append(order)

# Add incomplete data, outliers, duplicate data, and inconsistent date formats
for x in range(14):
    orders[random_index(len(orders)- 1)]['product_list'] = ''
    orders[random_index(len(orders)- 1)]['total_price'] = 10000
    orders[random_index(len(orders)- 1)]['customer_email'] = ''
    orders[random_index(len(orders)- 1)]['order_date'] = '01/2022/01 01:00:00'

for x in range(6):
    rand_index = random_index(len(orders)- 1)
    order_id_first_order = orders[rand_index]['order_id']
    other_rand_index = random_index(len(orders)- 1)
    if not rand_index == other_rand_index:
        print('order_id_first_order', order_id_first_order)
        orders[other_rand_index]['order_id'] = order_id_first_order

# Save sales dataset to CSV file
with open('sales_data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=[
                            'order_id', 'customer_email', 'product_list', 'total_price', 'order_date'])
    writer.writeheader()
    for order in orders:
        writer.writerow(order)
