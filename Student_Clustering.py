import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1 : Load The Dataset
df = pd.read_csv("student-mat.csv",sep=';')
print("First 5 Rows",df.head())

# Step 2 : Select Features
features = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
X = df[features]

# Step 3 : Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4 : Apply KMeans
KMeans = KMeans(n_clusters=3,random_state=42)
df['Cluster'] = KMeans.fit_predict(X_scaled)

# Step 5 : View Cluster Data
print("Cluster Counts",df['Cluster'].value_counts())
print("Cluster Centers",KMeans.cluster_centers_)

# Step 6 : Visualisation
plt.scatter(df['G3'],df['studytime'],c=df['Cluster'])
plt.xlabel("Final Grade (G3)")
plt.ylabel("Study Time")
plt.title("Student Clusters")
plt.show()

