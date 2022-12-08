import pandas as pd

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

# Function to JSONify a csv file
#
# Input: filename (string)
#
# Output: data (JSON object)
#


def jsonify_csv(filename):
    # Read the CSV file
    df = pd.read_csv(filename)
    # Convert the dataframe to a JSON object
    data = df.to_json(orient='records')
    # Return the JSON object
    return data
