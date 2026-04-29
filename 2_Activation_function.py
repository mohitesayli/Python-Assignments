import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

# Functions
sigmoid = 1 / (1 + np.exp(-x))
relu = np.maximum(0, x)
tanh = np.tanh(x)

# Plot
plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, relu, label="ReLU")
plt.plot(x, tanh, label="Tanh")

plt.legend()
plt.title("Activation Functions")
plt.show()