prompt = (f"Tickets: "
          f"\n\tUnder 3: Free"
          f"\n\t3-12: $10"
          f"\n\tOver 12: $15"
          f"\nPlease enter your age with digits (Not spelled out)."
          f"\nOnce done, enter quit ")

while True:
    age = input(prompt)
    if age == "quit":
        break
    elif int(age) < 3:
        print("Your ticket is free.")
    elif int(age) > 3 and int(age) < 13:
        print("Your ticket costs $10.")
    elif int(age) > 12:
        print("Your ticket costs $15.")