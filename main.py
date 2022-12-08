from extraction import *
from filtering import *

# Get data from Bugcrowd API
url = "https://bugcrowd.com/programs.json?sort[]=promoted-desc&page[]=0"
data = get_data(url)
# Filter the data and save it as a CSV file
filtered_data = filter_data(data)
save_as_csv(filtered_data, "bugcrowd_programs.csv")
