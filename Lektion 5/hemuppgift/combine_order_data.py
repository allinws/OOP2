import pandas as pd

order_data_1 = pd.read_csv("order_data_1.csv")
order_data_2 = pd.read_csv("order_data_2.csv")

combined_order_data = pd.merge([order_data_1, order_data_2], on='order_id')