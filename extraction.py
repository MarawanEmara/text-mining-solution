from urllib import request
from urllib.request import Request, urlopen
import json
import pandas as pd

# Function that gets a page from a URL
#
# Input: url (string)
#
# Output: page (string)
#


def get_page(url):
    # Add a user agent to the request to avoid 403 errors
    response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    # Read the response and convert it to a JSON object
    page = urlopen(response).read()
    # Return the page
    return page

# Function to get data from the API and return it as a JSON object
#
# Input: url (string)
#
# Output: data (JSON object)
#


def get_data(url):
    # Get the page from the URL
    page = get_page(url)
    # Convert the page to a JSON object
    data = json.loads(page)
    # Return the JSON object
    return data

# Function to get HTML from a URL
#
# Input: url (string)
#
# Output: html (string)
#


def get_html(url):
    # Get the page from the URL
    page = get_page(url)
    # Convert the page to a string
    html = page.decode("utf-8")
    # Return the string
    return html
