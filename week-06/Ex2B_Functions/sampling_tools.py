import random

products = [
'Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector'
]

random_product = random.choice(products)
print(f"Product of the Day: {random_product}")

three_products = random.sample(products, 3)
print(three_products)

random.shuffle(products)
print(products)

count = random.randint(50, 300)
print(f"Transaction count: {count}")