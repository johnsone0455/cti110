# Program to convert kilometers into miles
# 10/24/19
# CTI-110 P5T1_KilometerConverter
# Elizabeth Johnson

# Ask user to input kilometers
# Converter kilometers into miles
# Display miles

CONVERSION_FACTOR = 0.6214
def main():
    kilometers = float(input('Enter a distance in kilometers: '))
    show_miles(kilometers)
    
def show_miles(km):
    miles = km * 0.6214
    print(km, 'kilometers equals', miles, 'miles.')

main()
