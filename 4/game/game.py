import random

while True:
    lvl = input('Level: ')
    if lvl.isdigit() and int(lvl) > 0:
        break
n = int(lvl)
random_number = random.randint(1, n)
while True:
    guess_input = input('Guess: ')
    if guess_input.isdigit() and int(guess_input) > 0:
        guess = int(guess_input)
        if guess < random_number:
            print("Too small!")
        elif guess > random_number:
            print("Too large!")
        else:
            print("Just right!")
            break
    elif guess_input.isdigit() and int(guess_input) <= 0:
        print("Too small!")
