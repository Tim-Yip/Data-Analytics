a = 1
b = 19
c = 8

if a >= b and a >= c:
    max = a
elif b >= a and b >= c:
    max = b
else:
    max = c

print(f"The maximum value is {max}.")

if a <= b and a <= c:
    min = a
elif b <= a and b <= c:
    min = b
else:
    min = c

print(f"The minimum value is {min}.")