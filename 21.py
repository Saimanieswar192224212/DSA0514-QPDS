import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'BOB', 'cArL', 'dAvID']}
df = pd.DataFrame(data)

# Swap cases of the 'Name' column
df['Name'] = df['Name'].str.swapcase()

print(df)