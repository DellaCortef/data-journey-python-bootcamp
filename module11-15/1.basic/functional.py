import pandas as pd

def load_csv_and_filter(csv_file, state):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Check and remove empty cells
    df = df.dropna()
    
    # Filter the rows by the status column
    df_filtered = df[df['state'] ==state]
    
    return df_filtered

# Usage example
csv_file = './example.csv' # replace 'data.csv' with the path of your CSV file
filtered_state = 'SP' # state you want to filter
df_filtered = load_csv_e_filter(csv_file, filtered_state)

print(df_filtered)