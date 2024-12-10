# pipeline.py

import os
import glob
import pandas as pd

def read_and_combine_json(path: str) -> pd.DataFrame:
    """
    Reads all JSON files from the specified path and combines them into a single DataFrame.

    Parameters:
    path (str): Path to the folder containing JSON files.

    Returns:
    pd.DataFrame: Combined DataFrame containing data from all JSON files, or None if no files found.
    """
    if not os.path.isdir(path):
        print(f"The path '{path}' does not exist. Please check the path and try again.")
        return None
    
    json_files = glob.glob(os.path.join(path, '*.json'))
    if not json_files:
        print(f"No JSON files found in the path '{path}'.")
        return None

    df_list = [pd.read_json(file) for file in json_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def total_sales_sum(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the total sales by multiplying 'quantity' and 'amount' columns.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing sales data with 'quantity' and 'amount' columns.

    Returns:
    pd.DataFrame: DataFrame with a new 'total_sales' column added.

    Raises:
    ValueError: If the required columns are missing or the DataFrame is empty.
    """
    if df is None or df.empty:
        raise ValueError("The input DataFrame is empty or None.")

    required_columns = ["quantity", "amount"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"The required column '{col}' is missing from the DataFrame.")
    
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    if df["quantity"].isnull().any() or df["amount"].isnull().any():
        print("Warning: Some values in 'quantity' or 'amount' are missing or invalid. These will be treated as NaN.")
    
    df["total_sales"] = df["quantity"] * df["amount"]
    return df

def load_data(df: pd.DataFrame, data_folder: str = "data"):
    """
    Saves a DataFrame to both CSV and Parquet formats inside the specified data folder.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    data_folder (str): The folder where files will be saved (default: 'data').

    Returns:
    None
    
    Raises:
    IOError: If there is an issue saving the files.
    """
    if df is None or df.empty:
        raise ValueError("The input DataFrame is empty or None. Please provide a valid DataFrame.")

    output_folder = os.path.join(data_folder, "data_insights")
    os.makedirs(output_folder, exist_ok=True)

    csv_path = os.path.join(output_folder, "data_insights.csv")
    parquet_path = os.path.join(output_folder, "data_insights.parquet")

    try:
        df.to_csv(csv_path, index=False)
        print(f"Data successfully saved to CSV: {csv_path}")
    except Exception as e:
        raise IOError(f"An error occurred while saving the CSV file: {e}")
    
    try:
        df.to_parquet(parquet_path, index=False)
        print(f"Data successfully saved to Parquet: {parquet_path}")
    except ImportError:
        print("Parquet engine not available. Skipping Parquet file saving.")
    except Exception as e:
        raise IOError(f"An error occurred while saving the Parquet file: {e}")
