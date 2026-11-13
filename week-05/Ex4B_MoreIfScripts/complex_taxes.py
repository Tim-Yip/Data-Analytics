pay_rate = float(input("What is your pay rate? "))
hours_worked = float(input("How many hours did you work this week? "))
filing_status = input("What is your filing status, single or joint? ")

if hours_worked > 40:
    overtime_pay = (hours_worked - 40) * pay_rate * 1.5
    total_pay = 40 * pay_rate + overtime_pay
    annual_salary = total_pay * 52
else:
    total_pay = hours_worked * pay_rate
    annual_salary = total_pay * 52

if annual_salary < 12000 and filing_status == "single":
    tax = 0.05 * annual_salary
    net_pay = annual_salary - tax
elif annual_salary < 12000 and filing_status == "joint":
    net_pay = annual_salary
elif annual_salary >= 12000 and annual_salary < 25000 and filing_status == "single":
    tax = 0.1 * annual_salary
    net_pay = annual_salary - tax
elif annual_salary >= 12000 and annual_salary < 25000 and filing_status == "joint":
    tax = 0.06 * annual_salary
    net_pay = annual_salary - tax
elif annual_salary >= 25000 and annual_salary < 75000 and filing_status == "single":
    tax = 0.15 * annual_salary
    net_pay = annual_salary - tax
elif annual_salary >= 25000 and annual_salary < 75000 and filing_status == "joint":
    tax = 0.11 * annual_salary
    net_pay = annual_salary - tax
elif annual_salary >= 75000 and filing_status == "single":
    tax = 0.2 * annual_salary
    net_pay = annual_salary - tax
elif annual_salary >= 75000 and filing_status == "joint":
    tax = 0.2 * annual_salary
    net_pay = annual_salary - tax

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross pay is ${annual_salary:.2f}.")
print(f"Your filing status is {filing_status}.")
print(f"Your tax withholding for the week is ${tax:.2f}.")
print(f"Your net pay is ${net_pay:.2f}.")