import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.DataFrame({
    'customer_id': range(1, 101),
    'amount_spent': [100 * i for i in range(1, 101)],
    'items_purchased': [i for i in range(1, 101)]
})
customer_data = data.groupby('customer_id').agg({
    'amount_spent': 'sum',
    'items_purchased': 'sum'
}).reset_index()
features = customer_data[['amount_spent', 'items_purchased']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
inertia = []
for n in range(1, 11):
    kmeans = KMeans(n_clusters=n, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()
optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
customer_data['cluster'] = kmeans.fit_predict(scaled_features)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=customer_data, x='amount_spent', y='items_purchased', hue='cluster', palette='viridis')
plt.title('Customer Segments')
plt.xlabel('Total Amount Spent')
plt.ylabel('Total Items Purchased')
plt.legend(title='Cluster')
plt.show()
