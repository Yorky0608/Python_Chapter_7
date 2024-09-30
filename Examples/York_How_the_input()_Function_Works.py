#parrot.py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#greater.py
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#rollercoaster.py
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")