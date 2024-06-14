import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
data = {
    'Product_Category': ['Electronics','Clothing','Home appliances','Books','Toys','Beauty','Sports','Automotive'],
    'Total_Sales': [190000,8000,30000,310000,11000,21000,9000,50000]
}
df = pd.DataFrame(data)
print(df.head())
plt.figure(figsize=(10, 6))
plt.plot(df['Product_Category'], df['Total_Sales'], marker='o', linestyle='-', color='b')
plt.title('Total Sales by Product Category (Line Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Product_Category'], df['Total_Sales'], color='r')
plt.title('Total Sales by Product Category (Scatter Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df['Product_Category'], df['Total_Sales'], color='g')
plt.title('Total Sales by Product Category (Bar Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
