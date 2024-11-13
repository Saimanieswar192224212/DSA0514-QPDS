import pandas as pd
import numpy as np

# Create a dataframe with 10 rows and 4 columns of random values
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Convert some values to nan
df.iloc[0, 2] = np.nan
df.iloc[3, 3] = np.nan
df.iloc[4, 0] = np.nan
df.iloc[9, 2] = np.nan

# Define a function to apply the conditional formatting
def highlight_nan(val):
    color = 'red' if pd.isna(val) else 'black'
    return f'color: {color}'

# Apply the function to the entire dataframe
df_styled = df.style.applymap(highlight_nan)

# Display the styled dataframe
df_styled
