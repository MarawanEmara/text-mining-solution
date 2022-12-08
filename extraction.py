from urllib import request
from urllib.request import Request, urlopen
import json
import pandas as pd

# Function to get data from the API and return it as a JSON object
#
# Input: url (string)
#
# Output: data (JSON object)
#


def get_data(url):
    # Add a user agent to the request to avoid 403 errors
    response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    # Read the response and convert it to a JSON object
    page = urlopen(response).read()
    data = json.loads(page)
    # Return the JSON object
    return data

# Function to save the data as a CSV file
#
# Input: data (JSON object), filename (string)
#
# Output: None
#


def save_as_csv(data, filename):
    # Convert the JSON object to a pandas dataframe
    df = pd.DataFrame(data)
    # Save the dataframe as a CSV file
    df.to_csv(filename, index=False)
