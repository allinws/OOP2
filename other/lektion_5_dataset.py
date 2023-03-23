import csv

# Create a CSV file for customer orders
orders_header = ['OrderID', 'CustomerID', 'Product', 'Quantity', 'Price']
orders_rows = [    [1001, 101, 'Product A', 2, 10.99],
    [1002, 102, 'Product B', 1, 20.99],
    [1003, 103, 'Product C', 3, 5.99],
    [1004, 101, 'Product D', 2, 15.99],
    [1005, 104, 'Product E', 1, 25.99]
]

with open('customer_orders.csv', mode='w', newline='') as orders_file:
    orders_writer = csv.writer(orders_file)
    orders_writer.writerow(orders_header)
    orders_writer.writerows(orders_rows)

# Create a CSV file for customer details
details_header = ['CustomerID', 'Name', 'Address', 'Phone']
details_rows = [    [101, 'John Doe', '123 Main St', '555-1234'],
    [102, 'Jane Smith', '456 Elm St', '555-5678'],
    [103, 'Bob Johnson', '789 Oak St', '555-9012'],
    [104, 'Alice Brown', '321 Pine St', '555-3456']
]

with open('customer_details.csv', mode='w', newline='') as details_file:
    details_writer = csv.writer(details_file)
    details_writer.writerow(details_header)
    details_writer.writerows(details_rows)