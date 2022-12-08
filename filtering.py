# Function that takes in a program_url and appends a base_url to it
#
# Input: program_url (string), base_url (string)
#
# Output: url (string)
#
def get_program_url(program_url, base_url):
    # Combine the base URL and the program URL
    url = base_url + program_url
    # Return the new URL
    return url

# Function to filter the data and return the array of programs
# then further filter each dictionary in the array to return the
# name and URL of each program
#
# Input: data (JSON object)
#
# Output: programs (array)
#


def filter_data(data):
    # Get the array of programs from the JSON object
    programs = data['programs']
    # Return if there are no programs
    if not programs:
        return None
    # Create an empty array to store the filtered programs
    filtered_programs = []
    # Loop through each program in the array
    for program in programs:
        # Create a dictionary to store the filtered program
        filtered_program = {}
        # Add the name and URL to the dictionary
        filtered_program['name'] = program['name']
        filtered_program['url'] = get_program_url(
            program['program_url'], 'https://bugcrowd.com')
        # Add the dictionary to the array
        filtered_programs.append(filtered_program)
    # Return the array of filtered programs
    return filtered_programs
