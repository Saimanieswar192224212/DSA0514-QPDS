import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(100)
y = np.random.rand(100)

# Create a scatter plot with empty circles
plt.scatter(x, y, s=100, facecolors='none', edgecolors='blue')

# Customize the plot (optional)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Empty Circles')

# Show the plot
plt.show()