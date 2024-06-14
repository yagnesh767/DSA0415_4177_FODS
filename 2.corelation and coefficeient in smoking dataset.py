import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
data = {
    'Smoking_Habits': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    'Lung_Cancer_Rate': [1, 3, 4, 5, 7, 8, 9, 11, 13, 15]
}
df = pd.DataFrame(data)
print("Dataset:\n", df)
corr_coefficient, _ = pearsonr(df['Smoking_Habits'], df['Lung_Cancer_Rate'])
print(f"Correlation Coefficient: {corr_coefficient}")
plt.scatter(df['Smoking_Habits'], df['Lung_Cancer_Rate'], color='orange')
plt.title('Scatter Plot of Smoking Habits vs Lung Cancer Rate')
plt.xlabel('Smoking Habits (cigarettes per day)')
plt.ylabel('Lung Cancer Rate (per 1000 individuals)')
plt.grid(True)
plt.show()
