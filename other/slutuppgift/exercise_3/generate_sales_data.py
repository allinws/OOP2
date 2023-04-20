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
products = ['T-shirt', 'Jeans', 'Sneakers', 'Jacket', 'Watch', 'Belt', 'Sunglasses', 'Hat', 'Scarf', 'Wallet']
addresses = [
    '123 Main St, New York, NY',
    '456 Oak St, San Francisco, CA',
    '789 Maple St, Los Angeles, CA',
    '321 Elm St, Chicago, IL',
    '654 Pine St, Boston, MA',
    '987 Cedar St, Austin, TX',
    '246 Birch St, Seattle, WA',
    '135 Aspen St, Miami, FL',
    '864 Spruce St, Denver, CO',
    '798 Willow St, Atlanta, GA',
    '951 Palm St, Phoenix, AZ',
    '369 Redwood St, Portland, OR',
    '147 Cherry St, Philadelphia, PA',
    '258 Hickory St, Dallas, TX',
    '321 Walnut St, Houston, TX',
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
    customer_address = random.choice(addresses)
    product_count = random.randint(1, 5)
    product_list = random.sample(products, product_count)
    total_price = sum(random_price() for _ in range(product_count))
    order = {
        'order_id': order_id,
        'customer_address': customer_address,
        'product_list': ', '.join(product_list),
        'total_price': total_price,
        'order_date': order_date.strftime('%Y-%m-%d %H:%M:%S')
    }
    orders.append(order)

# Add incomplete data, outliers, duplicate data, and inconsistent date formats
for x in range(14):
    orders[random_index(len(orders)- 1)]['product_list'] = ''
    orders[random_index(len(orders)- 1)]['total_price'] = 10000
    orders[random_index(len(orders)- 1)]['customer_address'] = ''
    orders[random_index(len(orders)- 1)]['order_date'] = '2022/01/01 01:00:00'

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
                            'order_id', 'customer_address', 'product_list', 'total_price', 'order_date'])
    writer.writeheader()
    for order in orders:
        writer.writerow(order)