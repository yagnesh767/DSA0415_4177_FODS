import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
data = {
    'Age': [23, 25, 28, 33, 35, 36, 38, 40, 43, 48, 50, 52, 54, 55, 57, 58, 60, 63],
    'Fat': [9.5, 10.2, 11.5, 12.3, 14.1, 15.4, 17.2, 19.1, 21.3, 23.5, 24.7, 25.9, 26.8, 28.1, 30.0, 31.3, 33.2, 35.0]
}
df = pd.DataFrame(data)
m_a = df['Age'].mean()
me_a = df['Age'].median()
sd_a = df['Age'].std()

m_f = df['Fat'].mean()
me_f = df['Fat'].median()
sd_f = df['Fat'].std()

print("Mean age is ",m_a)
print("Median age is ",me_a)
print("Standard Deviation age is ",sd_a)

print("Mean fat is ",m_f)
print("Mean fat is ",me_f)
print("Mean fat is ",sd_f)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'])
plt.title('Boxplot of Age')
plt.subplot(1, 2, 2)
sns.boxplot(y=df['Fat'])
plt.title('Boxplot of %Fat')
plt.show()

plt.figure(figsize=(6, 6))
sns.scatterplot(x='Age', y='Fat', data=df)
plt.title('Scatter Plot of Age vs %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.show()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')
plt.subplot(1, 2, 2)
stats.probplot(df['Fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of %Fat')
plt.show()
