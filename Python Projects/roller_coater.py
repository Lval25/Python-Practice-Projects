print("Welcome to the Dungeon Drop!")
print("Before proceding we have a couple of questions to ask before you can potentially ride the rolller coaster!")

print("\n")
height = int(input("How tall are you in cm? "))
age = int(input("How old are you? "))
photo = input("Would you like a photo? Y or N : ").capitalize()
bill = 0

if height >= 120:
    if age >= 45 and age <= 55:
        bill += 0
    elif age < 12:
        bill += 5
    elif age <= 18:
        bill += 7
    else:
        bill += 12
    if photo == "Y":
        bill += 3

    print("\n")
    print(f"Your bill total is ${bill}.")
else:
    print("You aren't tall enough to ride sorry.")
    

    
