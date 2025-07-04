import random

# Game picks Random choice
comp_choice = random.randint(0, 2)

#Player chooses ther option
player_choice = int(input("What do you choose 0: Rock, 1: Paper, 2: Scirrors? "))

print(f"Computer Choose: {comp_choice}")
print(f"Player Choose: {player_choice}")

if player_choice >= 3 or comp_choice < 0:
    print("Invalid choice was made")
elif player_choice == 0 and comp_choice == 2:
    print("You Win!!")
elif player_choice == 2 and comp_choice == 0:
    print("You Lose...")
elif player_choice == comp_choice:
    print("Draw..")
elif player_choice > comp_choice:
    print("You Win!")
elif comp_choice > player_choice:
    print("You Lose...")

"""if player_choice == "0":
    if random_choice == "Rock":
        print("Draw")
    if random_choice == "Paper":
        print("You lose.")
    if random_choice == "Scissor":
        print("You Win.")

if player_choice == "1":
    if random_choice == "Rock":
        print("You win!")
    if random_choice == "Paper":
        print("Draw")
    if random_choice == "Scissor":
        print("You Lose.")

if player_choice == "2":
    if random_choice == "Rock":
        print("You Lose!")
    if random_choice == "Paper":
        print("You Win!")
    if random_choice == "Scissor":
        print("Draw.")"""
