import math

# Inputs
x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

# Step 1: Weighted sum
z = (w1 * x1) + (w2 * x2) + bias
print("Weighted Sum (z):", z)

# Step 2: Sigmoid
output = 1 / (1 + math.exp(-z))

# Step 3: Output
print("Final Output:", output)

# Step 4: Explanation
if output > 0.5:
    print("Output is closer to 1")
else:
    print("Output is closer to 0")