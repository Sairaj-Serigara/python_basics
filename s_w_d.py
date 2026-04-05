import random

bot=random.choice(["s","w","g"])
player=input("Enter your choice: ")
print(f"player -> {player} bot -> {bot}")
if player == "s":
    if bot=="g":
        print("Bot wins")
    elif bot=="w":
        print("player wins")
    else:
        print("Draw")
if player == "w":
    if bot=="s":
        print("Bot wins")
    elif bot=="g":
        print("player wins")
    else:
        print("Draw")

if player == "g":
    if bot=="s":
        print("player wins")
    elif bot=="w":
        print("bot wins")
    else:
        print("Draw")