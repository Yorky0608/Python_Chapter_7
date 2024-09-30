prompt = (f"Tickets: "
          f"\n\tUnder 3: Free"
          f"\n\t3-12: $10"
          f"\n\tOver 12: $15"
          f"\nPlease enter your ages and amount of tickets you wish to buy with digits (Not spelled out)."
          f"\nOnce done, enter quit \n")

print(prompt)
amount = int(input("amount "))
count = 0
cost = 0

while count < amount:
    age = input("\nage ")
    if int(age) < 3:
        print("Your ticket is free.")
    elif 3 < int(age) < 13:
        print("Your ticket costs $10.")
        cost += 10
    elif int(age) > 12:
        print("Your ticket costs $15.")
        cost += 15
    count += 1
print(f"${cost}")