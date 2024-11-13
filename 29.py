import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']

# Create a bar chart with different colors
plt.bar(languages, popularity, color=colors)

# Add labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Languages')

# Show the plot
plt.show()