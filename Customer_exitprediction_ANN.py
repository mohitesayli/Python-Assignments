import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

# Dataset (X = features)
X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 0],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

# Output (0 = stay, 1 = leave)
y = np.array([0,0,1,1,0,0,1,1,0,1])

# Step 1: Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Train model
model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000)
model.fit(X_scaled, y)

# Step 3: Test input
new_customer = np.array([[46, 1450, 5, 6, 9]])
new_scaled = scaler.transform(new_customer)

# Step 4: Prediction
prediction = model.predict(new_scaled)

if prediction[0] == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer will stay")