bank_balance = 0
savings_goal = 500
weekly_savings = 50

while bank_balance < savings_goal:
    bank_balance += weekly_savings
    if bank_balance > savings_goal / 2 and bank_balance < savings_goal * 0.75:
        print(f"Almost there! This week my balance is up to ${bank_balance}.")
    elif bank_balance > savings_goal * 0.75 and bank_balance < savings_goal:
        print(f"So close! After treating myself, my balance is up to ${bank_balance}.")
    elif bank_balance < savings_goal / 2:
        print(f"This week my balance increased to ${bank_balance}.")

print(f"Goal met! My current balance is ${bank_balance}.")