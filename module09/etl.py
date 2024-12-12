# etl.py

# Importing libs
from pipeline import read_and_combine_json, total_sales_sum, load_data

def etl_process(data_path: str):
    """
    Orchestrates the ETL process:
    - Extract data from JSON files
    - Transform data by calculating total sales
    - Load data into CSV and Parquet formats

    Parameters:
    data_path (str): Path to the folder containing JSON files
    """
    # Step 1: Extract data
    print("Starting the ETL process...")
    df = read_and_combine_json(data_path)
    if df is None:
        print("No data extracted. Exiting the ETL process.")
        return
    
    # Step 2: Transform data
    print("Transforming the data...")
    try:
        df = total_sales_sum(df)
    except ValueError as ve:
        print(f"Error during transformation: {ve}")
        return

    # Step 3: Load data
    print("Loading the data...")
    try:
        load_data(df, data_folder=data_path)
        print("ETL process completed successfully.")
    except IOError as ioe:
        print(f"Error during loading: {ioe}")

if __name__ == "__main__":
    # Define the folder containing JSON files
    data_path = "data"
    etl_process(data_path)
