import csv
import random
import datetime

products = [
    'A',
    'B',
    'C',
    'D',
    'E',
]

first_order_id = 1001

def random_date(start, end):
    return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

customer_ids = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]

orders_header = ['OrderID', 'CustomerID', 'Product', 'Quantity', 'Price']


start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2023, 3, 17)

order_rows = []
for x in range(10):
    order = [
        first_order_id + x,
        random.choice(customer_ids),
        random.choice(products),
        random_date(start_date, end_date)
    ]
    order_rows.append(order)

print(order_rows)



# with open('customer_orders.csv', mode='w', newline='') as orders_file:
#     orders_writer = csv.writer(orders_file)
#     orders_writer.writerow(orders_header)
#     orders_writer.writerows(orders_rows)

# # Create a CSV file for customer details
# details_header = ['CustomerID', 'Name', 'Address', 'Phone']
# details_rows = [    [101, 'John Doe', '123 Main St', '555-1234'],
#     [102, 'Jane Smith', '456 Elm St', '555-5678'],
#     [103, 'Bob Johnson', '789 Oak St', '555-9012'],
#     [104, 'Alice Brown', '321 Pine St', '555-3456']
# ]

# with open('customer_details.csv', mode='w', newline='') as details_file:
#     details_writer = csv.writer(details_file)
#     details_writer.writerow(details_header)
#     details_writer.writerows(details_rows)