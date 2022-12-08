from main_io import *
from filtering import *
from extraction import *

# Empty list to store the data
over_data = []
revisit = []
# Get data from Bugcrowd API
url = "https://bugcrowd.com/programs.json?page[]="
for page in range(1, 9999):
    # Add the page number to the URL
    new_url = url + str(page)
    print("Getting page " + new_url)
    # Get the data from the URL
    # If there's an error getting the data, add number
    # to revisit list and continue
    try:
        data = get_data(new_url)
    except:
        revisit.append(page)
        print("Error getting page " + str(page))
        continue
    # Filter the data and save it as a CSV file
    filtered_data = filter_data(data)
    if filtered_data is None:
        print("No more pages")
        break
    # Extend the filtered data to the list (includes flattened data)
    over_data.extend(filtered_data)
    print("Got page " + str(page))

# Save the data to a CSV file
save_as_csv(over_data, "bugcrowd_programs.csv")
