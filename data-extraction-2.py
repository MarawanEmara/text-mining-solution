import pandas as pd
from main_io import *
from strip_html import *

# Read the CSV file
bugcrowd_programs = "bugcrowd_programs.csv"
# Convert the CSV file to a JSON object
data = jsonify_csv(bugcrowd_programs)
print(data)
# print data type
print(type(data))

# Loop over the JSON object
for program in data:
    # Get the URL of the program
    url = program['url']
    # Get the HTML of the program
    html = get_html(url)
    # Get the "bounty-content" class from the HTML
    content = get_class(html, "bounty-content")
    # Strip the HTML tags from the class
    text = strip_tags(str(content))
    # Add the text to the JSON object
    program['details'] = text

# print(data)
# Save the JSON object as a CSV file
save_as_csv(data, "bugcrowd_programs_details.csv")
