# How do you calculate the distance between coordinates (x1, y1) and (x2, y2)?
x1 = float(input("What is the x-coordinate of the first point? "))
y1 = float(input("What is the y-coordinate of the first point? "))
x2 = float(input("What is the x-coordinate of the second point? "))
y2 = float(input("What is the y-coordinate of the second point? "))
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}.")