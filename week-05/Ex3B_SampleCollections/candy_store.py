candy = ("Skittles", "Starburst", "Jolly Ranchers")
flavors = ("Strawberry", "Orange", "Apple")

candy_options = {
    candy[0] + " " + flavors[1],
    candy[1] + " " + flavors[2],
    candy[2] + " " + flavors[0],
}

print("Today's candy options include:")
print(candy_options)
#Running the script multiple times will display the combinations in a different order each time. 