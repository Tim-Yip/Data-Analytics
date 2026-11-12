# You are going to tile a room whose dimensions are length by width feet. There are
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
# can only buy full boxes, not a partial box.
# You also want to buy at least 10% more tiles than you need in order to handle chips,
# breakage, and mess-ups. How many total boxes will you buy?

length = float(input("What is the length of the room? "))
width = float(input("What is the width of the room? "))
boxes = (length * width * 1.1) // 12
print(f"You will buy {boxes} boxes of tiles.")