
import numpy as np
import matplotlib.pyplot as plt

# Create an array of discrete values for n
n_values = np.arange(0, 64, 1)  # Adjust the range and step size as needed

# Compute the corresponding values of cos(n/8 - pi)
cos_values = np.cos(n_values / 8 - np.pi)

# Create the plot
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(n_values, cos_values, marker='o', linestyle='-')
plt.title('Plot of cos(n/8 - pi)')
plt.xlabel('n')
plt.ylabel('cos(n/8 - pi)')
plt.grid(True)
plt.show()
