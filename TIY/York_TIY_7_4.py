prompt = f"Please enter a topping you want on your pizza. \nEnter quit to end. "

while True:
    topping = input(prompt)
    if topping != "quit":
        print(f"Adding {topping} to the pizza.")
    else:
        break