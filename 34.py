import matplotlib.pyplot as plt
import numpy as np

# Generate random data for x, y coordinates and sizes
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.randint(100, 500, 50)

# Create a scatter plot with varying sizes
plt.scatter(x, y, s=sizes, alpha=0.7)

# Customize the plot (optional)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Varying Sizes')

# Show the plot
plt.show()