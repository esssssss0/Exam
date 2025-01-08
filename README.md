# DSDE1-Computing1 Assessment 2 Instructions

This is an open book/computer/internet asssessment. You are allowed to refer to your own notes, previous code, and search online. You are **NOT** allowed to receive or ask for assistance from any individual such as a fellow classmate or anyone else including AI-assistants like GitHub Co-Pilot. You may NOT share your code with anyone else until all students have completed the assessment and submission has closed. Any violations will be treated as academic misconduct which may result in receiving zero marks for the assessment.

If a test file will be used to mark the code that you write, that test file is provided so that you can test your code yourself. Note that all code will be also evaluated with PyLint, so you are encouraged to use PyLint to evaluate your own code before the final submission.

## How to Complete the Assessment

1. Clone this repository on your own computer.

2. Commit your answers and push them to your repo on GitHub. You can (and are encouraged) to do this continuously as you work on the questions.

3. Ensure that you are correctly pushing your changes to the repo by checking on GitHub for your changes.

4. Your final answers must be pushed by the deadline at **11:50 (1 hour and 50 minutes after the timed start)** unless you have been explicitly allowed extended time as a reasonable adjustment as recommended by the Disability Advisory Services (students for whom this applies have been contacted). You will have 5 minutes to make the final push to GitHub (until 11:55 for the standard assessment time). Any pushed commits after this time will not be considered for marks. **If you cannot successfully push to GitHub, then you must email a zip file of your submission to Becky (r.stewart@imperial.ac.uk) before the end of the assessment time.** If you have trouble doing this, then raise your hand to let the invigilators know.

5. If you do not use git to push your code to the correct repository within the allotted assessment time (e.g. the GitHub upload button is used instead of pushing a commit), you will have a penalty of 10% applied to your overall score.

## Marking Rubrics

Detailed marking rubrics can be seen at the top of the Python or text file for each question. 


## Assessment Questions

### Reading and Understanding Code *[20 points available]*
1. Try to run the code and use the class in `question1.py` in the folder `question1`. Fix the problems in the code using the docstring and comments as guidance so that it runs without throwing any errors and passes the test file `test_question1.py`.    *[10 points]*

2. Draw the UML class diagram for the class in Question 1. Use the contents of the text file `question2.txt` in the `question2` folder as a template. Carefully read the additional instructions at the top of the file.    *[10 points]*


### Data manipulation and plotting *[30 points]*
3. Using pandas, write a function called `get_publisher_stats()` with one input parameter for the publisher. Have the function import `question3_table.csv` from the csv folder and filter for the books with that publisher. It should then return the median of the average rating (the column from the csv) and median number of text reviews for those filtered books. If the publisher is not found in the csv, then a ValueError is raised.   *[10 points]*


4. Write a method called `add_genre_column()` that imports `question4_table.csv` from the local csv folder and adds a column to the imported table called the genre name specified in the input parameter. The new column contains `True` if the specified genre name appears in the genre column for that row and `False` if it does not. The table with the new column is returned.   *[10 points]*


5. Write a script that creates the same plot as shown in `question5_plot.png` based on the data from `question5_table.csv` in the local csv folder. The theme is dark and the x axis tick labels are manually set to the matching month 1 in the csv file to 'Jan' and so on. Use the function documented at: [https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot)  *[10 points]*

![Plot for Question 5](question5/question5_plot.png)


### Flow Charts *[10 points]*
6. In the file `question6.py` create a function called `flowchart()` that implements the flowchart in `question6.png`. Use the test file in the folder `question6` to check if your implementation is correct.    *[10 points]*

![Flowchart for Question 6](question6/question6.png)


### Writing Python Classes *[40 points]*
7. Create a new class and a second class that extends the first following the instructions in the comments in the file `question7.py` in the folder `question7`. Use the test files in the folder `question7` to check if your implementation is correct.    *[40 points]*