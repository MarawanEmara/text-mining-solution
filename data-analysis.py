import pandas as pd
from main_io import *
from strip_html import *

# Read the CSV file
bugcrowd_programs = "bugcrowd_programs.csv"
# Convert the CSV file to a JSON object
data = jsonify_csv(bugcrowd_programs)

