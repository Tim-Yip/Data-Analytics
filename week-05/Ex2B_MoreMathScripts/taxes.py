# Federal taxes are 23% of your salary every month. You make X amount of money. How much is withheld for taxes?
salary = float(input("What is your monthly pay? "))
federal_taxes = salary * 0.23
print(f"${federal_taxes:.2f} is withheld for federal taxes.")