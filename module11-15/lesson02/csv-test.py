# Importing the pandas library for data manipulation and analysis
import pandas as pd

# Reading data from a CSV file named 'example.csv' into a DataFrame
df = pd.read_csv('./example.csv')

# Filtering the DataFrame to include only rows where the 'state' column equals 'SP'
df_filtered = df[df['state'] == 'SP']

# Overwriting the previous filter to include only rows where the 'price' column equals '10.50'
# Note: This overwrites the previous filtering on 'state' and may not be intentional.
df_filtered = df[df['price'] == '10.50']

# Printing the filtered DataFrame (after filtering by 'price')
print(df_filtered)

# Reading data from another CSV file named 'example2.csv' into a DataFrame
df2 = pd.read_csv('./example2.csv')

# Filtering the second DataFrame to include only rows where the 'state' column equals 'DF'
df_filtered2 = df2[df2['state'] == 'DF']

# Overwriting the previous filter to include only rows where the 'price' column equals '10.50'
# Similar to the first case, this overwrites the earlier filter on 'state'.
df_filtered2 = df2[df2['price'] == '10.50']

# Printing the filtered DataFrame (after filtering by 'price')
print(df_filtered2)
