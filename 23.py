import matplotlib.pyplot as plt
import numpy as np

# Read data from the text file
data = np.loadtxt('test.txt')

# Extract x and y values
x = data[:, 0]
y = data[:, 1]

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot from Text File')

# Show the plot
plt.show()