import csv

# Pull in the CSV file
filename = 'Chapter_7 Challenge.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    names = []
    candy_type_1 = []
    candy_type_2 = []
    candy_price_1 = []
    candy_price_2 = []

    for row in reader:
        name = row[1]
        candy_1 = row[2]
        candy_2 = row[4]
        price_1 = float(row[3])
        price_2 = float(row[5])

        # add the code here that will append each variable above into the correct list.

        names.append(name.title())
        candy_type_1.append(candy_1.title())
        candy_type_2.append(candy_2.title())
        candy_price_1.append(price_1)
        candy_price_2.append(price_2)


students_candy = {}

while True:
    if not names:
        break
    students_candy[names.pop(0)] = {"Candy" : [candy_type_1.pop(0),candy_type_2.pop(0)], "Price" : [candy_price_1.pop(0), candy_price_2.pop(0)]}


while True:
    student = input("\nWhat is your name?  ")
    student = student.title()
    if student in students_candy:
        print(students_candy[student])

        while True:

            remove_add = input("\nDo you want to remove or add a candy? remove/add/no ")
            remove_add = remove_add.title()

            if remove_add == "No":
                break

            elif remove_add == "Remove":
                remove = input("\nWhat candy do you want to remove?  ")
                remove = remove.title()
                for i in range(0, len(students_candy[student]["Candy"])):
                    if students_candy[student]["Candy"][i] == remove:
                        print(f"You removed {students_candy[student]["Candy"].pop(i)} that costed ${students_candy[student]["Price"].pop(i)}.")

            elif remove_add == "Add":
                add = input("\nWhat type of candy do you want to add?  ")
                add = add.title()
                students_candy[student]["Candy"].append(add)
                price = float(input("\nWhat is the price of the candy?  "))
                students_candy[student]["Price"].append(price)
                print(f"You added {add} that costs {price}.")

        total_price = 0

        for amount in students_candy[student]["Price"]:
            total_price += amount
        print(f"\nYour bill for all your candies is ${total_price}")
        print("Your responses were added to the survey.")


    else:
        print(f"Sorry {student}, you are not in the list.")