# CTI-110
# P3HW1 - Month number
# Elizabeth Johnson
# 9/24/2019

# Get user to input the number of the month
# Display the name of the month based on the number
# Display error if number inputted is outside of 1-12 

month = int(input('Enter a number that corresponds with a month: '))
if month == 1:
    print('January')
elif month == 2:
    print('February')
elif month == 3:
    print('March')
elif month == 4:
    print('April')
elif month == 5:
    print('May')
elif month == 6:
    print('June')
elif month == 7:
    print('July')
elif month == 8:
    print('August')
elif month == 9:
    print('September')
elif month == 10:
    print('October')
elif month == 11:
    print('November')
elif month == 12:
    print('December')
else:
    print('Sadly the number you have entered corresponds with a month that has not been invented yet. Please reload the program and try again with the number of a month that exists in the Greogrian calendar. Those numbers would be 1-12.')
