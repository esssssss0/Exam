'''
question6.py


TOTAL POINTS AVAILABLE: 10 


Code Functionality (7)
7 points - desired plot is generated and code is efficient and Pythonic

5-6 points - desired plot is generated, but code could be significantly 
improved to be more Pythonic

3-4 points - plot has some errors

1-2 points - no plot is generated, but some effort was made to generate one

0 points - no effort made to answer question



Code Readability (3)
3 points - Well commented, clear code 

1-2 points - Some issues related to comments or issues such as variable 
names could be improved 

0 points - multiple and repeated significant style issues, code very 
difficult to understand
'''

# Create a function called flowchart() that implements the flowchart
# in `question6.png`. Use the test file in the folder `question6` to
# check if your implementation is correct.

def flowchart(input_list):

    # Check if input_list is None
    if input_list is None:
        return {}

    # Check if all elements in input_list are strings
    if all(isinstance(item, str) for item in input_list):
        # Create a dictionary with counts of each unique string
        return {item: input_list.count(item) for item in set(input_list)}

    # If input_list contains non-string elements, return input_list unchanged
    return input_list


# Trials
print(flowchart(None))
print(flowchart(["apple", "banana", "apple"]))
print(flowchart(["apple", 123, "banana"]))
