import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    'day': range(1, 31),
    'sales': np.random.randint(50,200,size=30)
}
sales_data = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
plt.plot(sales_data['day'], sales_data['sales'], marker='o', linestyle='-')
plt.title('Sales Over Time')
plt.xlabel('Day of the Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(sales_data['day'], sales_data['sales'], color='blue')
plt.title('Sales Over Time')
plt.xlabel('Day of the Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(sales_data['day'], sales_data['sales'], color='green')
plt.title('Sales Over Time')
plt.xlabel('Day of the Month')
plt.ylabel('Sales')
plt.grid(axis='y')
plt.show()