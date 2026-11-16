food = ["sushi", "noodles", "pizza", "chicken", "steak"]

for index, item in enumerate(food, start = 1):
    print(f"{index}. {item}", end = " ")
    if index == 1:
        print("<- top pick!")
    else:
        print()