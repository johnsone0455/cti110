# Python program to ask for bugs collected and then display total
# 10/8/19
# CTI-110 P4T2 - Bug Collector
# Elizabeth Johnson

# Get bugs collected each day from user
# Calculate the total number of bugs from all days
# Display the total number of bugs collected

bugTotal = 0
for day in range(1, 6):
    print('Enter the number of bugs collected on day', day)
    bugs = int(input())
    bugTotal += bugs
print('You collected', bugTotal, 'total bugs after five days.')
