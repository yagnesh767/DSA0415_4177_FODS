import numpy as np
sales_data = np.array([
    [100, 150, 200],
    [250, 300, 350],
    [400, 450, 500]
])
print("Sales Data:")
print(sales_data)
average_price = sales_data.mean()
print(f"\nAverage price of all products sold in the past month: ${average_price:.2f}")
