# Using decision structures with rectangle areas
# 9/19/19
# CTI-110 P3T1 - Areas of Rectangles
# Elizabeth Johnson

# Ask for the length and widths of two rectangles
# Calculate the areas
# Use the if statement to determine if there is a size difference
# Display area and tell which rectangle is larger or if they are equal

lengthA = float(input('Enter the length of the first rectangle: '))
widthA = float(input('Enter the width of the first rectangle: '))
lengthB = float(input('Enter the length of the second rectangle: '))
widthB = float(input('Enter the width of the second rectangle: '))
rectangleA_area = lengthA * widthA
rectangleB_area = lengthB * widthB
print(rectangleA_area)
print(rectangleB_area)
if rectangleA_area > rectangleB_area:
    print('The first rectangle entered has the larger area.')
elif rectangleA_area < rectangleB_area:
    print('The second rectangled entered has the larger area.')
else:
    print('The rectangles are equal in area.')
