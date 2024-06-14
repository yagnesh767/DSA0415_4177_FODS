import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    'customer_id': range(1, 101),
    'age': np.random.randint(18, 70, size=100)
}
sales_data = pd.DataFrame(data)
print("Sales Data:")
print(sales_data.head())
age_frequency = sales_data['age'].value_counts().sort_index()
print("\nFrequency Distribution of Ages:")
print(age_frequency)
plt.figure(figsize=(12, 6))
age_frequency.plot(kind='bar')
plt.title('Frequency Distribution of Customer Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()
