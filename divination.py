import random

print("************************")
print("Welcome adivination game")
print("************************")

number = random.randint(1, 3)
response = int(input("Enter a number: "))

if response == number:
    print("Congratulations, you got it right")
else:
    print("You missed")
