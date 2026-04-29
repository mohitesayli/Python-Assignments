# Inputs
x = 2
w = 0.5
bias = 0.1
target = 1
learning_rate = 0.01

# Step 1: Prediction
y_pred = w * x + bias
print("Prediction:", y_pred)

# Step 2: Error
error = y_pred - target
print("Error:", error)

# Step 3: Update weight
w_new = w - learning_rate * error * x

# Step 4: Update bias
bias_new = bias - learning_rate * error

print("Old Weight:", w)
print("Updated Weight:", w_new)

print("Old Bias:", bias)
print("Updated Bias:", bias_new)