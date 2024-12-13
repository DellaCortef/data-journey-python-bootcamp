import schedule
import time
from lib.classes.CsvSource import CsvSource
from lib.classes.JsonSource import JsonSource
from lib.classes.TxtSource import TxtSource

# Function to check new files
def check_for_new_files():
    csv_source.check_for_new_files() # Calls the instance's check_for_new_files method
    txt_source.check_for_new_files()
    json_source.check_for_new_files()

# Scheduling the execution of the check_for_new_files() function every second
schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSource()
txt_source = TxtSource()
json_source = JsonSource()

# Run the main loop
while True:
    schedule.run_pending()
    time.sleep(1) # Wait 1 second so that the loop does not consume too much processing