import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
bugcrowd_programs_bounty = "bugcrowd_programs_bounty.csv"
# Convert the CSV file to a JSON object
data = pd.read_csv(bugcrowd_programs_bounty)

# Plot two separate histograms of the minimum and maximum bounty values
# rounded to the nearest 1000
sns.histplot(data['min_bounty'].round(-3), kde=False, label='Minimum')
sns.histplot(data['max_bounty'].round(-3), kde=False, label='Maximum')
# Add a legend
plt.legend()
# Show the plot
plt.show()
