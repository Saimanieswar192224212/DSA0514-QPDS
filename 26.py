import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create multiple subplots
plt.subplot(2, 1, 1)  # 2 rows, 1 column, first subplot
plt.plot(x, y1)
plt.title('Sine Wave')

plt.subplot(2, 1, 2)  # 2 rows, 1 column, second subplot
plt.plot(x, y2)
plt.title('Cosine Wave')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()