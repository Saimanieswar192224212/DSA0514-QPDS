import matplotlib.pyplot as plt
import numpy as np

# Sample data
means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)

# Create bar plot with different colors
x = np.arange(len(means_men))
width = 0.35

plt.bar(x, means_men, width, label='Men')
plt.bar(x + width, means_women, width, label='Women')

# Add labels and title
plt.xlabel('Group')
plt.ylabel('Score')
plt.title('Scores by Group and Gender')
plt.xticks(x + width / 2, ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'])
plt.legend()

# Show the plot
plt.show()