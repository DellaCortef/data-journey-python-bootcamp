import pandas as pd

class ETLProcess:
    def __init__(self, data_source):
        self.data_source = data_source

    def extract_data(self):
        raise NotImplementedError("Extract_data method must be implemented in child classes.")

    def transform_data(self, data):
        raise NotImplementedError("Transform_data method must be implemented in child classes.")

    def load_data(self, transformed_data):
        raise NotImplementedError("Load_data method must be implemented in child classes.")

    def execute_etl(self):
        extracted_data = self.extract_data()
        transformed_data = self.transform_data(extracted_data)
        self.load_data(transformed_data)

class ETLCSV(ETLProcess):
    def extract_data(self):
        return pd.read_csv(self.source_data)

    def transform_data(self, data):
        # Simple transformation example: convert all letters to uppercase
        return data.applymap(lambda x: x.upper() if isinstance(x, str) else x)

    def load_data(self, transformed_data):
        # Here you can implement the logic to load the transformed data from a CSV file
        print("Transformed data (CSV):")
        print(transformed_data)


class ETLExcel(ETLProcess):
    def extract_data(self):
        return pd.read_excel(self.source_data)
    
    def transform_data(self, data):
        # Simple transformation example: convert all letters to lowercase
        return data.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    def load_data(self, transformed_data):
        # Here you can implement the logic to load the transformed data from an Excel file
        print("Transformed data (Excel):")
        print(transformed_data)


# Usage example
if __name__ == "__main__":
    source_csv = 'dados.csv' # Replace 'dados.csv' with the path of your CSV file
    etl_csv = ETLCSV(source_csv)
    etl_csv.executar_etl()

    excel_source = 'dados.xlsx' # Replace 'dados.xlsx' with the path of your Excel file
    etl_excel = ETLExcel(excel_source)
    etl_excel.executar_etl()