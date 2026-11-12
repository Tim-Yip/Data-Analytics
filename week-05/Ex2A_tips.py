# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
# print("The total due is " + str(total_due))
# The string function is to convert the data type to a string and it is used
# here so the total price can be displayed.

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Total due is " + str(total_due))
print("Tip is " + format(tip, ".2f"))