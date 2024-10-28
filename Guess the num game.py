
import random
print("GUESS THE NUMBER GAME")
num = random.randint(1,20)

guess = int(input("Enter the number that you guess? That is below 20 :"))

attempts = 4
current_attempt = 0


while num != guess and current_attempt < attempts - 1:
    current_attempt += 1
    if num < guess:
        print("your number is higher")
    else:
        print("your number is lower")
    guess = int(input("Enter the number again:"))

if num==guess:
    print("You won !!")
else:
    print("You Lost..")