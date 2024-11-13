import matplotlib.pyplot as plt
import numpy as np

# Sample marks of 10 students in Mathematics and Science
math_marks = np.array([85, 92, 78, 89, 95, 72, 88, 90, 83, 87])
science_marks = np.array([90, 88, 82, 93, 97, 75, 85, 92, 80, 86])

# Create a scatter plot
plt.scatter(math_marks, science_marks)

# Customize the plot
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Mathematics vs. Science Marks')

# Show the plot
plt.show()