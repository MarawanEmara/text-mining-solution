from bs4 import BeautifulSoup
from io import StringIO
from html.parser import HTMLParser
from extraction import *


# This class is used to strip HTML tags from a string
# It is used in the strip_tags function below


class MLStripper(HTMLParser):
    # Initialize the class
    def __init__(self):
        super().__init__()
        self.reset()
        # Convert HTML entities like &gt; to their corresponding characters
        self.strict = False
        # Convert character references like &gt; to their corresponding characters
        self.convert_charrefs = True
        # Create a string to store the data
        self.text = StringIO()
    # Handle data

    def handle_data(self, d):
        self.text.write(d)
    # Get the data

    def get_data(self):
        return self.text.getvalue()


# Function to get a certain class from an HTML string
#
# Input: html (string), class_name (string)
#
# Output: class_data (array)
#


def get_class(html, class_name):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')
    # Get the class from the HTML
    class_data = soup.find_all(class_=class_name)
    # Unpack the array and return the first element
    return class_data[0]


# Function to strip HTML tags from a string
#
# Input: html (string)
#
# Output: s.get_data() (string)
#


def strip_tags(html):
    # Create an instance of the MLStripper class
    s = MLStripper()
    # Feed the HTML to the MLStripper object
    s.feed(str(html))
    # Return the data
    return s.get_data()
