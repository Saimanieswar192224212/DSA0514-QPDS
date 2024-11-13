import pandas as pd

# Manually define the data
data = {
    'Column1': [1, 2, 3, 4, 5],
    'Column2': ['A', 'B', 'C', 'D', 'E'],
    'Column3': [10.5, 20.3, 30.7, 40.1, 50.2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the dimensions (shape) of the DataFrame
print("Shape of the DataFrame:", df.shape)

# Extract and print the column names
column_names = df.columns
print("Column Names:", column_names)
