import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
plt.plot(x, y1, label='Sine', linewidth=2, color='blue')
plt.plot(x, y2, label='Cosine', linewidth=3, color='red')

# Add labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Multiple Line Plot')

# Add legend
plt.legend()

# Show the plot
plt.show()