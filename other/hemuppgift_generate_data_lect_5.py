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


customer_ids = [x for x in range(0,23)]

customer_emails = [
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

customer_data = []

for x, y in zip(customer_ids, customer_emails):
    customer = {
        'customer_id': x,
        'customer_email': y
    }
    customer_data.append(customer)




# Define order count and date range
order_count = 1000
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 3, 17)

# Generate sales dataset
orders = []
for i in range(order_count):
    order_date = random_date(start_date, end_date)
    order_id = i + 1
    customer_id = random.choice(customer_ids)
    product_count = random.randint(1, 5)
    product_list = random.sample(products, product_count)
    total_price = round(sum(random_price() for _ in range(product_count)),2)
    order = {
        'order_id': order_id,
        'customer_id': customer_id,
        'product_list': ', '.join(product_list),
        'total_price': total_price,
        'order_date': order_date.strftime('%m/%d/%Y %H:%M:%S')
    }
    orders.append(order)

# Add incomplete data, outliers, duplicate data, and inconsistent date formats
for x in range(14):
    orders[random_index(len(orders)- 1)]['product_list'] = ''
    orders[random_index(len(orders)- 1)]['total_price'] = 10000
    orders[random_index(len(orders)- 1)]['customer_id'] = ''
    orders[random_index(len(orders)- 1)]['order_date'] = '2022/01/01 01:00:00'

for x in range(6):
    rand_index = random_index(len(orders)- 1)
    order_id_first_order = orders[rand_index]['order_id']
    other_rand_index = random_index(len(orders)- 1)
    if not rand_index == other_rand_index:
        orders[other_rand_index]['order_id'] = order_id_first_order

# Save sales dataset to CSV file
with open('order_data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=[
                            'order_id', 'customer_id', 'product_list', 'total_price', 'order_date'])
    writer.writeheader()
    for order in orders:
        writer.writerow(order)


with open('customer_details.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=[
                            'customer_id', 'customer_email',])
    writer.writeheader()
    for order in customer_data:
        writer.writerow(order)