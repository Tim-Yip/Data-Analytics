radius = float(input("What is the radius of the circle? "))
area = 3.14 * radius ** 2
print("The area of a circle with radius " + str(radius) + " is " + format(area, ".2f"))
# A pitfall of using the input() function is that if the user enters a word instead of a number, it will give an error.