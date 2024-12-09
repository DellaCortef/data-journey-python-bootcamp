# main.py

from challenge import read_csv, process_data, calculate_sales_category

if __name__ == "__main__":
    # Step 1: Ask the user for the CSV file path
    file_path = input("Please enter the path to the CSV file: ").strip()

    # Step 2: Read data from the CSV file
    sales_items = read_csv(file_path)
    if not sales_items:
        print("No data to process. Exiting...")
        exit()

    # Step 3: Process data
    processed = process_data(sales_items)
    print("\nProcessed Data:")
    print(processed)

    # Step 4: Calculate sales by category
    sales_by_category = calculate_sales_category(processed)
    print("\nTotal Sales by Category:")
    print(sales_by_category)
