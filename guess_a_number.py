import random

attempts = 0
secret_number = random.randrange(99) + 1  # Integer from 0 to 98 inclusive + 1 -> we generate a number between 1 and 99
print("Let's play a game. You should guess a secret number.")
while True:
    guess = 100
    try:
        guess = int(input("Your guess:"))
        attempts = attempts + 1
    except ValueError:
        print("You are dumb bitch. It's not a number.")
    if guess == secret_number:
        print("Congratulations. You win. You did " + str(attempts) + " attempts.")
        break
    elif guess < secret_number:
        print("Nope. The secret number should be bigger.")
    elif guess > secret_number:
        print("Nope. The secret number should be less.")
