'''
question5.py

TOTAL POINTS AVAILABLE: 10 

Code Functionality (7)
7 points - desired plot is generated and code is efficient and Pythonic

5-6 points - desired plot is generated, but code could be significantly 
improved to be more Pythonic

3-4 points - plot has some errors

1-2 points - no plot is generated, but some effort was made to generate one

0 points - no effort made to answer question



Code Readability (3)
3 points - Well commented, clear code where PyLint returns no or 
few errors/warnings

2 points - Missing either docstring or comments

1 point - Comments or documentation missing and variable names
could be improved 

0 points - multiple and repeated significant style issues, code very 
difficult to understand
'''

# Write a script that creates the same plot as shown in question5_plot.png
# based on the data from question5_table.csv in the local csv folder. The
# theme is dark and the x axis tick labels are manually set to the matching
# month 1 in the csv file to 'Jan' and so on.
#
# Use the function documented at:
# https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Allow access to the data from the CSV file
data = pd.read_csv('question5/csv/question5_table.csv')

# Create a dictionary to map months to their abbreviations
month_map = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',
    6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',
    11: 'Nov', 12: 'Dec'
}

# Replace the month numbers with their corresponding abbreviations
data['Month'] = data['Month'].map(month_map)

# Set the dark theme
sns.set_theme(style="dark")

# Create the scatter plot
plt.figure(figsize=(6, 6))
sns.scatterplot(data=data, x='Month', y='Avg_Price')

# Add title and labels
plt.title("Distribution of Average Price by Month")
plt.xlabel("Month")
plt.ylabel("Price")

# Show the plot
plt.tight_layout()
plt.show()
