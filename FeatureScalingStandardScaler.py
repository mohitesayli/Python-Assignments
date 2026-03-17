import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

data = [
    [25,20000],
    [30,40000],
    [35,80000]
]

scaler = StandardScaler()

scaled_data = scaler.fit(data)

print("Original Data : ",data)

print("scaled data : ", scaled_data)

#-------------------------------------
# Euclidean distance before scaling
#-------------------------------------
X = data[0]
Y = data[1]

distance_before = euclidean(X, Y)
#-------------------------------------
# Euclidean distance after scaling
#-------------------------------------
X_scaled = data[0]
Y_scaled = data[1]

distance_after = euclidean(X_scaled, Y_scaled)

print("\nEuclidean Distance before scaling:", distance_before)
print("Euclidean Distance after scaling:", distance_after)