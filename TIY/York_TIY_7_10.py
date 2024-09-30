results = {}

promtp = f"\nWhat is your name?  "
promtp2 = f"If there was one place you could vist, where would you visit?  "

while True:
    name = input(promtp)
    place = input(promtp2)
    results[name] = place

    quit = input("Do others want to take the survey? y/n  ")
    if quit == "n":
        break
    else:
        pass

for name, place in results.items():
    print(f"\n{name} wanted to go to {place}.")