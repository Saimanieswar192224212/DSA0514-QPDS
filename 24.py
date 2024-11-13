import pandas as pd
import matplotlib.pyplot as plt

# Read financial data from CSV
df = pd.read_csv('fdata.csv')

# Plot the 'Close' price over time
plt.plot(df['Date'], df['Close'])

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Alphabet Inc. Stock Price')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()