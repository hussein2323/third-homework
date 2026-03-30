import random

def random_number():
    return random.randint(1, 100)

def guess(target):
    while True:
        guess = int(input("Guess the number (1-100): "))
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print("good job  ")
            break

number_to_guess = random_number()
guess(number_to_guess)