def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    return(f"{city}, {state} {zip}")

def add_numbers(*numbers):
    total = sum(numbers)
    equation = " + ".join(str(num) for num in numbers)
    return(f"{equation} = {total}")

def display_receipt(total_due, amount_paid):
    change = amount_paid - total_due
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    if change >= 0:
        return(f"Change Due: ${change:.2f}")
    else:
        return(f"Remaining Balance: ${abs(change):.2f}")

print(display_mailing_label("John Doe", "123 Main St", "Anytown", "CA", "12345"))
print()
print(display_mailing_label("Jane Smith", "456 Oak Ave", "Othertown", "NY", "67890"))
print()

print(add_numbers(5))
print(add_numbers(10, 20))
print(add_numbers(1, 2, 3, 4, 5))
print()

print(display_receipt(50.00, 100.00))
print()
print(display_receipt(50.00, 50.00))
print()
print(display_receipt(100.00, 50.00))