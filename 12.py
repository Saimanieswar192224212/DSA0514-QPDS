import pandas as pd
import numpy as np

# Generate random data
data = {
    'A': np.random.randn(10),
    'B': np.random.randn(10),
    'C': np.random.randn(10),
    'D': np.random.randn(10),
    'E': np.random.randn(10)
}

# Create DataFrame
df = pd.DataFrame(data)

# Apply styling for HTML output
styled_df = df.style.set_properties(**{'background-color': 'black', 'color': 'yellow'})

# Export to HTML for web display
styled_df.to_html('styled_dataframe.html')

# Print a message to guide the user
print("The styled DataFrame has been saved to 'styled_dataframe.html'. Please open it in a web browser to view the colors.")