dept_code = int(input("Enter your department code: "))

if dept_code == 1:
    print("Marketing")
elif dept_code == 5:
    print("Human Resources")
elif dept_code == 10:
    print("Accounting")
elif dept_code == 12:
    print("Legal")
elif dept_code == 18:
    print("IT")
elif dept_code == 20:
    print("Customer Relations")
else:
    print("Invalid department code")

dept_code = int(input("Enter your department code: "))
match dept_code:
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        print("Invalid department code")