import math

# Example values
y_true = 1
y_pred = 0.9

# MSE
mse = (y_true - y_pred) ** 2
print("MSE:", mse)

# Binary Cross Entropy
bce = -(y_true * math.log(y_pred) + (1 - y_true) * math.log(1 - y_pred))
print("Binary Cross Entropy:", bce)