# Calculate Student Grades
    # 5/3/21
    # CTI-110 P3HW1 - Debugging
    # Yazmyne West
    #

# This program takes a number grade and outputs a letter grade.
# system uses 10-point grading scale

    
# Begin program

# Put in the total score in to determine student's grade

score = float(input('Enter score: '))

if score >= 90:
    print('Your grade is: A')
elif score >= 80:
    print('Your grade is: B')
elif score >= 70:
    print('Your grade is: C')
elif score >= 60:
    print('Your grade is: D')
elif (score <= 59) and (score >= 0):
    print('Your grade is: F')
else:
    print('Invalid. Please enter a positive number')


# End of program
