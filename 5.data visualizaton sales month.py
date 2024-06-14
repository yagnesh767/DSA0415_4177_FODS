import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [250, 220, 340, 280, 300, 330, 360, 390, 400, 420, 410, 450]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='c')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.xticks(rotation=45)  
plt.ylabel('Sales')
plt.grid(axis='y')  
plt.tight_layout()
plt.show()
