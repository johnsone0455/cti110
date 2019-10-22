# Calculation of meal total
# 9/10/19
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Elizabeth Johnson

# Get meal total, tip percent, totals from user
# Calculate actual tip and tax totals, then calculate the meal total including tip and tax
# If given incorrect tip percent, display error and allow user to reenter correct percentage
# Display tip, tax, and meal totals

meal_charge = float(input('Enter meal total:'))
print('Please choose which percent amount you will use: 16%, 18%, or 20%:')
tip_chosen = int(input('Tip percent:' '%'))
if tip_chosen == 16:
    print('Thank you for your tip!')
    tip = tip_chosen
    tip_percent = tip/100
    tax = 6
    tax_percent = tax/100
    tip_total = meal_charge * tip_percent
    tax_total = meal_charge * tax_percent
    print('The tip is $', format(tip_total, ',.2f'))
    print('The tax is $', format(tax_total, ',.2f'))
    meal_total = meal_charge + tip_total + tax_total
    print('The meal total is $', format(meal_total, ',.2f'))
elif tip_chosen == 18:
    print('Thank you for your tip!')
    tip = tip_chosen
    tip_percent = tip/100
    tax = 6
    tax_percent = tax/100
    tip_total = meal_charge * tip_percent
    tax_total = meal_charge * tax_percent
    print('The tip is $', format(tip_total, ',.2f'))
    print('The tax is $', format(tax_total, ',.2f'))
    meal_total = meal_charge + tip_total + tax_total
    print('The meal total is $', format(meal_total, ',.2f'))
elif tip_chosen == 20:
    print('Thank you for your tip!')
    tip = tip_chosen
    tip_percent = tip/100
    tax = 6
    tax_percent = tax/100
    tip_total = meal_charge * tip_percent
    tax_total = meal_charge * tax_percent
    print('The tip is $', format(tip_total, ',.2f'))
    print('The tax is $', format(tax_total, ',.2f'))
    meal_total = meal_charge + tip_total + tax_total
    print('The meal total is $', format(meal_total, ',.2f'))
else:
    print('That percent is not available. The program will choose a percent for you.')
    import random
    list = [16,18,20]
    tip = random.choice(list)
    print('The program has chosen this tip: %',tip)
    tip_percent = tip/100
    tax = 6
    tax_percent = tax/100
    tip_total = meal_charge * tip_percent
    tax_total = meal_charge * tax_percent
    print('The tip is $', format(tip_total, ',.2f'))
    print('The tax is $', format(tax_total, ',.2f'))
    meal_total = meal_charge + tip_total + tax_total
    print('The meal total is $', format(meal_total, ',.2f'))
