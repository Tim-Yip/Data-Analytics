# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay).
# How many vans do you need? 
# How much will it cost to rent vans?
# What is the cost if you split it per person?

import math

people = int(input("How many people are going on the tour? "))
vans = math.ceil(people / 15)
total_cost = vans * 250
cost_per_person = total_cost / people
print(f"You need {vans} vans.")
print(f"The total cost is ${total_cost:.2f}.")
print(f"The cost per person is ${cost_per_person:.2f}.")