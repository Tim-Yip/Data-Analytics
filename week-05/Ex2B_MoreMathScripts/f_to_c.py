# How do you convert a temperature from Fahrenheit to Celsius?
f = float(input("What is the temperature in Fahrenheit? "))
c = (f - 32) * 5 / 9
print(f"{f}°F is equal to {c:.2f}°C.")