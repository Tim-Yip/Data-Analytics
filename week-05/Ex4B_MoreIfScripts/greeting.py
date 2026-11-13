hour = 26

if hour < 10 and hour >= 4:
    print("Good morning")
elif hour >= 10 and hour < 17:
    print("Good day!")
elif hour >= 17 and hour < 23:
    print("Good evening")
elif hour < 4 or hour >= 23 and hour < 25:
    print("What are you doing up so late??")
elif hour >= 25:
    print("Invalid hour")