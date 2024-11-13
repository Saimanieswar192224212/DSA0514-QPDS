import matplotlib.pyplot as plt
import numpy as np

# Data for three groups
group1_weight = np.array([56, 58, 60, 62, 64, 66, 68, 70, 72])
group1_height = np.array([100, 120, 140, 160, 180, 130, 160, 220, 240])

group2_weight = np.array([57, 59, 61, 63, 65, 67, 69, 71])
group2_height = np.array([110, 130, 150, 170, 120, 150, 190, 170])

group3_weight = np.array([58, 60, 62, 64, 66, 68, 70])
group3_height = np.array([120, 140, 160, 180, 130, 170, 160])

# Create a scatter plot for each group
plt.scatter(group1_weight, group1_height, label='Group 1', color='blue')
plt.scatter(group2_weight, group2_height, label='Group 2', color='red')
plt.scatter(group3_weight, group3_height, label='Group 3', color='green')

# Customize the plot
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Group-wise Weight vs Height Scatter Plot')
plt.legend()

# Show the plot
plt.show()