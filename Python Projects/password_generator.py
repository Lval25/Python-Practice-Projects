import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#GEt the amount of characters per element
let = int(input("How mant letters do you want? "))
num = int(input("How many number do you want? "))
sym = int(input("How mant symbols do you want? "))

#Initiate a empty password variable to
passwrd = ""



for i in range(let + 1):
    #For how ever many i's that are chosen add a letter character
    rand_let = random.choice(letters)
    passwrd += rand_let

for i in range(num + 1):
    rand_num = random.choice(numbers)
    passwrd += rand_num

for j in range(sym + 1):
    rand_sym = random.choice(symbols)
    passwrd += rand_sym

print("\n")
#Print the password as generated before shuffle
print(f"Straight password: {passwrd}")
print("\n")

#Turn the string into a list
rand_passwrd = list(passwrd)
#Shuffle the list of characters
random.shuffle(rand_passwrd)
#Join the list back into a string
rnd_pass = ''.join(rand_passwrd)
#Print the shuffled string
print(f"Shuffled Password: {rnd_pass}")
