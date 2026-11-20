f = open("about_me.txt", "r")

# print(f.read(50)) # .read(50) only prints out 50 characters. 
# print(f.read(50))

# print(f.readline(10))
# print(f.readline())

# for i in range(1, 5):
#     print(f.readline())

# print(f.readlines()) # displays all lines like a list

# print(f.readlines(1)) # displays only first line like a list

# print(f.readlines(10)) # displays only first line like a list

# print(f.readlines(100)) # displays only some lines like a list

# print(f.readlines(-1)) # displays all lines like a list

read50 = f.read(50)

readline = []
for i in range(4):
    readline.append(f.readlines(100))

readlines100 = f.readlines(100)

print("First 50 characters: ", read50)
print("Next four lines, as list by line: ", readline)
print("Nedxt 100 characters, as list by line, rounded up to complete lines: ", 
      readlines100)

f.close()