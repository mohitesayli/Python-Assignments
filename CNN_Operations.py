import numpy as np

# ==========================================
# 1. CONVOLUTION
# ==========================================
print("===== CONVOLUTION =====")

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [4
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

feature_map = []

for i in range(3):
    row = []
    for j in range(3):
        sum_val = 0
        for ki in range(3):
            for kj in range(3):
                sum_val += image[i+ki][j+kj] * kernel[ki][kj]
        row.append(sum_val)
    feature_map.append(row)

print("Feature Map:")
for r in feature_map:
    print(r)


# =======================================
# 2. ReLU + MAX POOLING
# =======================================
print("\n===== ReLU + MAX POOLING =====")

feature_map_np = np.array(feature_map)

# ReLU
relu_output = np.maximum(0, feature_map_np)
print("ReLU Output:\n", relu_output)

# Max Pooling (2x2)
pooled = []
for i in range(relu_output.shape[0] - 1):
    row = []
    for j in range(relu_output.shape[1] - 1):
        region = relu_output[i:i+2, j:j+2]
        row.append(np.max(region))
    pooled.append(row)

print("Pooled Output:")
for r in pooled:
    print(r)


# ======================================
# 3. FLATTENING
# ======================================
print("\n===== FLATTENING =====")

matrix = np.array([
    [6, 4],
    [8, 6]
])

flatten_output = matrix.flatten()
print("Flatten Output:", flatten_output)