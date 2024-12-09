# challenge.py

import csv
from typing import List, Dict


def read_csv(file_path: str) -> list[dict]:
    """
    Function that reads a CSV file and returns a list of dictionaries.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list[dict]: List of dictionaries representing the CSV rows.
    """
    try:
        # Open the file and read its contents
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        return rows
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []


def process_data(data: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """
    Process the data into a dictionary where the key is the category, 
    and the value is a list of dictionaries containing product information.

    Args:
        data (List[Dict[str, str]]): List of dictionaries representing the rows of the CSV file.

    Returns:
        Dict[str, List[Dict[str, str]]]: Processed dictionary grouped by category.
    """
    processed_data = {}

    for row in data:
        category = row.get("category")
        product_info = {
            "Product": row.get("product"),
            "Quantity": int(row.get("quantity", 0)),
            "Amount": float(row.get("amount", 0.0)),
        }

        if category not in processed_data:
            processed_data[category] = []
        processed_data[category].append(product_info)
    
    return processed_data


def calculate_sales_category(processed_data: Dict[str, List[Dict[str, str]]]) -> Dict[str, float]:
    """
    Calculate total sales for each category.

    Args:
        processed_data (Dict[str, List[Dict[str, str]]]): Processed dictionary grouped by category.

    Returns:
        Dict[str, float]: Total sales by category.
    """
    sales_by_category = {}

    for category, products in processed_data.items():
        total_sales = sum(product["Quantity"] * product["Amount"] for product in products)
        sales_by_category[category] = round(total_sales, 2)

    return sales_by_category
