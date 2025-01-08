'''
question3.py


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

# Using pandas, write a function called get_publisher_stats() with
# one input parameter for the publisher. Have the function import
# 'question3_table.csv' from the csv folder and filter for the books
# with that publisher. It should then return the median of the average
# rating (the column from the csv) and median number of text reviews for
# those filtered books. If the publisher is not found in the csv, then
# a ValueError is raised.

import pandas as pd

# Function to retrieve the median average rating and the numbre of text reviews
# for a specified publisher
def get_publisher_stats(publisher):

    # Load the data from the CSV file
    data = pd.read_csv('question3/csv/question3_table.csv')

    # Filter the data for the specified publisher
    filtered_data = data[data['publisher'] == publisher]

    # Raise ValueError if no books for the specified publisher are found
    if filtered_data.empty:
        raise ValueError(f"No books found for publisher: {publisher}")

    # Calculate the median of average rating and the median number of text reviews
    median_rating = filtered_data['average_rating'].median()
    median_text_reviews = filtered_data['text_reviews_count'].median()

    return median_rating, median_text_reviews

# Trial
median_rating, median_text_reviews = get_publisher_stats("Oxford University Press")
print(f"Median Average Rating: {median_rating}")
print(f"Median Number of Text Reviews: {median_text_reviews}")
