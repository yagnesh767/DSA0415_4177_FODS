import pandas as pd
data = {
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': ['C001', 'C002', 'C001', 'C003', 'C004'],
    'ProductID': ['P001', 'P002', 'P001', 'P003', 'P002'],
    'Quantity': [2, 1, 3, 5, 2],
    'TotalPrice': [200, 150, 300, 500, 300]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nDataFrame Info:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
total_revenue = df['TotalPrice'].sum()
print(f'\nTotal Revenue: ${total_revenue}')
popular_products = df.groupby('ProductID')['Quantity'].sum().sort_values(ascending=False)
print('\nMost Popular Products:')
print(popular_products)
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False)
print('\nTop Customers:')
print(top_customers)
average_quantity = df['Quantity'].mean()
print(f'\nAverage Order Quantity: {average_quantity}')
average_price = df['TotalPrice'].mean()
print(f'Average Order Price: ${average_price}')
