from urllib import request
from urllib.request import Request, urlopen
import json
import pandas as pd
import re

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

# Function to get all numbers following a $ sign in a string
#
# Input: string (string)
#
# Output: numbers (list)
#


def get_numbers(string, sign="$"):
    # New list to store the numbers
    numbers = []
    # Split string by sign
    string = string.split(sign)
    for item in string:
        # Search from the beginning of the string for numbers
        # Detects numbers that are either 3 digits long or 1-3 digits followed by a comma and 3 digits
        item = re.search(
            r"([^\d]|^)\d{1,3},\d{3}([^\d]|$)|([^\d]|^)\d{3}([^\d]|$)", item)
        # Convert re.Match object to a string
        item = item.group(0) if item else None
        # If there are no numbers, continue to the next item
        if item is None:
            continue
        # Remove all non-number characters
        item = re.sub(r"[^\d]", "", item)
        # Change each item to an integer
        item = int(item)
        # Add the number to the list
        numbers.append(item)
    # Return the list of numbers
    return numbers
