from interface.classes.csv_class import CsvProcessor
# import pandas as pd

csv_file = './example.csv'
filter = 'state'
limit = 'SP'

CSV_file = CsvProcessor(csv_file)
CSV_file.load_csv() # Load the CSV
print(CSV_file.filter_by(['state', 'price'], ['SP', '10.50']))
# print(file_CSV.df)
print("#########################")
#csv2_file = './example2.csv'
#filter2 = 'state' # Changed to filter2
# limit2 = 'DF'

# CSV2_file = CsvProcessor(csv2_file)
# CSV2_file.load_csv() # Load the CSV
# print(CSV2_file.filter_by(filter2, limit2)) # Changed to filter2
# print(file_CSV2.sub_filter('price', '10.50'))