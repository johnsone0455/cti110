# CTI-110
# P4HW1 - Expenses
# Elizabeth Johnson
# 10/8/19

# Get expense amount and title from user
# Ask user if second expense is to be entered, using if statement to continue program
# Continue the program until the user inputs 'n'
# Display how much is left in the account after expenses

Amount = float(input('Please enter the starting value in the account: '))
expenseNumber = int(input('How many expenses are you inputting today? '))
expenseAmount = float(input('Enter the amount for the expense: '))
expenseName = input('What is the name for this expense: ')
keep_going = input('Are you entering another expense? (y/n) ')
while keep_going == 'y':
        expenseAmount = expenseAmount + float(input('Enter the amount for the expense: '))
        expenseName = input('What is the name for this expense: ')
        keep_going = input('Are you entering another expense? (y/n) ')
        
print('The amount of expenses entered today was: ',expenseNumber)
print('The amount in the account before expenses was: ',Amount)
endAmount = Amount - expenseAmount
print('The amount in the account after expenses is: ',endAmount)
    
