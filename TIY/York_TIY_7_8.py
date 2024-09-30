sandwich_orders = ["Cold Cut Sub", "Pizza Wich", "Burger"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\n{sandwich} has been made.")
    finished_sandwiches.append(sandwich)

print("\nSandwiches made:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")