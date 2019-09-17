# Calculation of meal total
# 9/10/19
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Elizabeth Johnson

meal_charge = float(input('Enter meal total:'))
tip = float(input('Enter tip percent for server:%'))
tip_percent = tip/100
tax = float(input('Enter tax percent amount:%'))
tax_percent = tax/100
tip_total = meal_charge * tip_percent
tax_total = meal_charge * tax_percent
print('The tip is $', format(tip_total, ',.2f'))
print('The tax is $', format(tax_total, ',.2f'))
meal_total = meal_charge + tip_total + tax_total
print('The meal total is $', format(meal_total, ',.2f'))

# Input meal charge
# Input tip
# Convert tip to percent
# Input tax
# Convert tax to percent
# Calculate tip
# Calculate tax
# Display tip
# Display tax
# Calculate meal total
# Display meal total
