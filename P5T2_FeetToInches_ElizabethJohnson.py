# Program to convert feet to inches
# 10/31/19
# CTI-110 P5T1_FeetToInches
# Elizabeth Johnson

# Ask user to input feet
# Converter feet to inches
# Display inches

INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter a number of feet: '))
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
    
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
main()
