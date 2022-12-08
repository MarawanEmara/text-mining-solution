import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
bugcrowd_programs_bounty = "bugcrowd_programs_bounty.csv"
# Convert the CSV file to a JSON object
data = pd.read_csv(bugcrowd_programs_bounty)
# Remove all rows with missing values
data = data.dropna()

for i in ['min_bounty', 'max_bounty']:
    # Convert the values in the column to integers
    data[i] = data[i].astype(int)
    # Round all values in the column to the nearest 1000
    data[i] = data[i].round(-3)
    # Plot a histogram of the values in the column using matplotlib
    plt.hist(data[i], bins=20)
    # Set the title of the plot
    plt.title(i)
    # Show the plot
    plt.show()
    # Save the plot as a PNG file
    plt.savefig(i + ".png")
