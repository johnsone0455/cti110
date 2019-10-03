# CTI-110
# P3LAB - Debugging
# Elizabeth Johnson
# 10/1/19

# Get score from user
# Use if statments to calculate the letter grade
# Display the letter grade

A_score = 90
B_score = 80
C_score = 70
D_score = 60
yourScore = float(input('Enter a score: '))

if yourScore >= A_score:
    print('Your grade is an A.')
elif yourScore >= B_score:
    print('Your grade is a B.')
elif yourScore >= C_score:
    print('Your grade is a C.')
elif yourScore >= D_score:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

