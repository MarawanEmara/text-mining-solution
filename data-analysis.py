import pandas as pd
from main_io import *
from strip_html import *
from analysis_functions import *

# Read the CSV file
bugcrowd_programs_details = "bugcrowd_programs_details.csv"
# Convert the CSV file to a JSON object
data = jsonify_csv(bugcrowd_programs_details)

# Loop over the JSON object
for program in data:
    # Get the details of the program
    details = program['details']
    # Get the numbers from the details
    numbers = get_numbers(details)
    # Get the minimum and maximum values
    min, max = get_min_max(numbers)
    # Add the minimum and maximum values to the JSON object
    program['min_bounty'] = min
    program['max_bounty'] = max
    # Remove the details from the JSON object
    del program['details']
    # Print how many programs are left
    print(len(data) - data.index(program))

# Save the JSON object as a CSV file
save_as_csv(data, "bugcrowd_programs_bounty.csv")
