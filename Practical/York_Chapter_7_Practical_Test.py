places = []

count = 0

while count < 5:
    place  = input("Name a fast-food restaurant.  ").title()
    places.append(place)
    count += 1

diction = {}
count = 0

while count < 8:
    name = input("\nWhat is your name?  ").title()
    continue_ = ""
    list_of_restaurants = []
    #quit = ""
    while True:
        if continue_ == "n":
            break
        else:
            restaurant = input("Name a fast-food restaurant.  ").title()
            list_of_restaurants.append(restaurant)
        continue_ = input("Do you have more fast-food restaurants you want to add? y/n  ").lower()
    diction[name] = list_of_restaurants
    #quit = input("Is anyone else taking the survey? y/n  ").lower()
    #if quit == "n":
        #break
    count += 1

for restaurant in diction.values():
    for rest in restaurant:
        if rest not in places:
            places.append(rest)

print(places)
print(diction)
