import pandas as pd

class ProcessorCSV:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = None
    
    def load_csv(self):
        # Load the CSV file into a DataFrame
        self.df = pd.read_csv(self.arquivo_csv)
    
    def remove_empty_cells(self):
        # Check and remove empty cells
        self.df = self.df.dropna()
    
    def filter_by_state(self, state):
        # Filter the rows by the status column
        self.df = self.df[self.df['state'] == state]
    
    def process(self, state):
        # Load CSV, remove empty cells and filter by state
        self.load_csv()
        self.remove_empty_cells()
        self.filter_by_state(state)
        
        return self.df

# Usage example
csv_file = './example.csv' # replace 'example.csv' with the path of your CSV file
filtered_state = 'SP' # state you want to filter

processor = ProcessorCSV(csv_file)
df_filtered = processor.process(filtered_state)

print(df_filtered)