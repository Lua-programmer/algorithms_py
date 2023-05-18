import random

print("************************")
print("Welcome adivination game")
print("************************")

number = random.randint(1, 10)
response = int(input("Enter a number: "))

hit = response == number
smaller = response > number
bigger = response < number

if hit:
    print("Congratulations, you got it right")
elif bigger:
    print("You kicked up")
elif response:
    print("you kicked down")
