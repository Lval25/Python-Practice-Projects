print("Welcome to Pizza Picker!")
size = input("What soze pizza would you like? S, M or L: ").capitalize()
pepperoni = input("Would you like pepperoni? Y or N: ").capitalize()
extra_cheese = input("Do you want extra cheese? Y or N: ").capitalize()
pizza = 0

if size == "S":
    pizza = 15.00
elif size == 'M':
    pizza = 20.00
else:
    pizza = 25.00

if pepperoni == "Y":
    if size == "S":
        pizza += 2.00
    else:
        pizza += 3.00

if extra_cheese == "Y":
    pizza += 1.00
else:
    pizza += 0.00

print("\n")
print(f"The cost of you pizza is ${pizza:.2f}.")

