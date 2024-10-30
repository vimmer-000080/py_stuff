import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x, k):
    return np.sin(x) * np.sin(k * x) * np.sin(b * x)

# Generate x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Plot the function for different values of k
plt.figure(figsize=(12, 8))

k = 15
y = f(x, k)
plt.plot(x, y, label=f'k = {k}')

# Plot sin(x) and -sin(x) for reference
plt.plot(x, np.sin(x), 'k--', label='sin(x)')
plt.plot(x, -np.sin(x), 'k--', label='-sin(x)')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function confined between sin(x) and -sin(x) with periodic behavior')
plt.legend()
plt.grid(True)
plt.show()

