movies = ["Avatar", "Totoro", "Spirited Away", "Top Gun", "Ford v Ferrari"]
print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)

print(sorted(movies))
print(movies)

movies.sort()
print(movies)
#There is no difference between the two.

movies.append("Finding Nemo")
print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)