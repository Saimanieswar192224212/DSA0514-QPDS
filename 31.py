import matplotlib.pyplot as plt
import numpy as np

# Sample data
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_men = [4, 3, 4, 1, 5]
std_women = [3, 5, 2, 3, 3]

# Create bar plot with error bars
fig, ax = plt.subplots()

x = np.arange(len(means_men))  # the label locations
width = 0.35  # the width of the bars

rects1 = ax.bar(x, means_men, width, label='Men', yerr=std_men, capsize=10)
rects2 = ax.bar(x + width, means_women, width, label='Women', yerr=std_women, capsize=10)

# Add some text for labels, title, and custom x-axis ticks
ax.set_ylabel('Scores')
ax.set_xlabel('Groups')
ax.set_title('Scores by group and gender')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(['Group1', 'Group2', 'Group3', 'Group4', 'Group5'])
ax.legend()

fig.tight_layout()
plt.show()