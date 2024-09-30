sandwich_orders = ["pastrami", "Cold Cut Sub","pastrami", "Pizza Wich", "Burger", "pastrami"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != "pastrami":
        print(f"\n{sandwich} has been made.")
        finished_sandwiches.append(sandwich)
    else:
        print(f"\nWe are all out of {sandwich}.")

print("\nSandwiches made:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")