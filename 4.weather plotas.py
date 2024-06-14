import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [10, 12, 15, 20, 25, 28, 30, 29, 26, 22, 17, 12],
    'Rainfall': [50, 40, 30, 20, 10, 5, 5, 10, 15, 25, 40, 45]
}
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Temperature'], marker='o', color='blue', label='Temperature')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Rainfall'], marker='o', color='green', label='Rainfall')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Temperature'], df['Rainfall'], color='red')
plt.title('Temperature vs Rainfall')
plt.xlabel('Temperature (°C)')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.tight_layout()
plt.show()
