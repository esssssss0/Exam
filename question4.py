'''
question4.py


TOTAL POINTS AVAILABLE: 10 

Code Functionality (7)
7 points - all tests pass and code uses if/else, for structures in a 
Pythonic manner without relying on elements like pass or break or 
range() unnecessarily

5-6 points - all tests pass, but code could be significantly 
improved to be more Pythonic

3-4 points - at least one test fails, but code would work with small
changes

1-2 points - no test passes and effort has been made to answer question 
but would need significant changes/additions to function correctly

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

# Write a method called add_genre_column() that imports
# 'question4_table.csv' from the local csv folder and adds a column
# to the imported table called the genre name specified in the input
# parameter. The new column contains True if the specified genre name
# appears in the genre column for that row and False if it does not.
# The table with the new column is returned.

import pandas as pd

def add_genre_column(genre_name):

    data = pd.read_csv('question4/csv/question4_table.csv')

    # Add a new column with True/False based on the presence of the genre_name
    data[genre_name] = data['genre'].str.contains(genre_name, case=False, na=False)

    return data

# Trial
updated_data = add_genre_column("Fantasy")
print(updated_data)
