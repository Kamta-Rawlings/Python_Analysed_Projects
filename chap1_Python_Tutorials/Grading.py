'''
Docstring for chap1-Introduction.Grading
Take in the grades from the user using the 
input function and print out the following statement 
based on the above grading scheme

“Your grade of Y earns you an X in this course”

where X stands for one of the four letter grades,
A to D, and Y is the grades received as input from
the user, which you can assume will always be between
to 1
.

[Hint: use if statements.]
'''
A -> 90 and above
B -> 70 and above
C -> 50 and above
D -> 0-50

grade = input(int("Enter the student grade: "))
if grade > 70:
    if grade > 90:
        print (f'Your grade of {grade} earns you an A in this course')
    else:
        print (f'Your grade of {grade} earns you an A in this course')
elif grade > 50:
    print
    