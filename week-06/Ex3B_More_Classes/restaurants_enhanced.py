class Restaurant:

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served += customers

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            rating = input("How would you rate your experience today on a "
            "scale of 1-5 (5 being excellent)? ")
            if rating in ["1", "2", "3", "4", "5"]:
                rating = int(rating)
                break
            else:
                print("Invalid rating. Please enter an integer from 1-5.")
        self.customer_ratings.append(rating)
        average = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f"Your rating was {rating}. The average rating for this restaurant "
        f"is {average:.2f}.")

restaurant1 = Restaurant("In-N-Out", "Burgers")
restaurant2 = Restaurant("DH Noodles", "Noodles")
restaurant3 = Restaurant("Uncle Cha", "Chinese Fusion")

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()

for restaurant in [restaurant1, restaurant2, restaurant3]:
    restaurant.print_num_served()
    restaurant.add_num_served()
    restaurant.add_num_served()
    restaurant.add_num_served()
    restaurant.print_num_served()
    print()

for restaurant in [restaurant1, restaurant2, restaurant3]:
    restaurant.customer_rating()
    restaurant.customer_rating()
    restaurant.customer_rating()
    print()
