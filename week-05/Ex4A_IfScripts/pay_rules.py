pay_rate = float(input("What is your pay rate? "))
hours_worked = float(input("How many hours did you work? "))

if hours_worked > 40:
    overtime_pay = (hours_worked - 40) * pay_rate * 1.5
    total_pay = 40 * pay_rate + overtime_pay
else:
    total_pay = hours_worked * pay_rate

print(f"Your total pay is: ${total_pay:.2f}")