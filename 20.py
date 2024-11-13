mport pandas as pd

# Sample DataFrame
data = {'text': ['This is a sample text.', 'Another sample text with substring.', 'No substring here.']}
df = pd.DataFrame(data)

# Substring to search for
substring = 'sample'

# Function to find the index of the substring in a string
def find_substring_index(text, substring):
    index = text.find(substring)
    return index if index != -1 else None

# Apply the function to the 'text' column and create a new column 'substring_index'
df['substring_index'] = df['text'].apply(lambda x: find_substring_index(x, substring))

# Filter rows where the substring is found
df_filtered = df[df['substring_index'].notnull()]

print(df_filtered)
