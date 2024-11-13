import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
x = np.linspace(0, 10, 100)
y = 2 * x + 1

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Line Plot')

# Show the plot
plt.show()