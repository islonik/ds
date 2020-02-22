import random
import numpy as np

LO_BORDER = 1   # constant, DO NOT reassign
HI_BORDER = 100 # constant, DO NOT reassing

def manual_guess_a_number():
    attempts = 0
    secret_number = random.randrange(99) + 1  # Integer from 0 to 98 inclusive + 1 -> we generate a number between 1 and 99
    print("Let's play a game. You should guess a secret number.")
    while True:
        guess = HI_BORDER
        try:
            guess = int(input("Your guess:"))
            attempts += 1
        except ValueError:
            print("You are dumb bitch. It's not a number.")
        if guess == secret_number:
            print("Congratulations. You win. You did " + str(attempts) + " attempts.")
            break
        elif guess < secret_number:
            print("Nope. The secret number should be bigger.")
        elif guess > secret_number:
            print("Nope. The secret number should be less.")


def dumb_guess_a_number(number):
    # attempt to guess a random number using random
    # we generate a new random number each time
    attempts = 0
    while True:
        predict = np.random.randint(LO_BORDER, HI_BORDER)  # we generate a number between 1 and 100
        attempts += 1
        if number == predict:
            break
    return (attempts)


def incremental_guess_a_number(number):
    # attempt to guess a random number using incremental approach
    # we increase or decrease our number by 1
    attempts = 0
    predict = np.random.randint(LO_BORDER, HI_BORDER)
    while number != predict:
        attempts += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return (attempts)


def binary_search_guess_a_number(number):
    return binary_search_guess_a_number_with_range(number, LO_BORDER, HI_BORDER)

def binary_search_guess_a_number_with_range(number, lowest_range, highest_range):
    # attempt to guess a random number using binary search
    number = range_correction(number)
    lowest_range = range_correction(lowest_range)
    highest_range = range_correction(highest_range)
    # core logic
    attempts = 0
    predict = round((highest_range - lowest_range) / 2)
    while number != predict:
        attempts += 1
        if number > predict:
            lowest_range = predict
            predict = predict + round((highest_range - predict) / 2)
        elif number < predict:
            highest_range = predict
            # fix corner case with number = 1 and predict = 2
            temp = predict
            predict = round((predict + lowest_range) / 2)
            if predict == temp:
                predict -= 1
        predict = range_correction(predict)
    return (attempts)

def range_correction(number):
    # validation
    if number > HI_BORDER:
        number = HI_BORDER
    elif number < LO_BORDER:
        number = LO_BORDER
    return number

def score_game(function_name):
    # run it n (> 100) times, to find out how fast we could guess a number
    count_ls = []
    np.random.seed(1)  # setup RANDOM SEED, for science and repeatability
    random_array = np.random.randint(LO_BORDER, HI_BORDER, size=(10000))
    for number in random_array:
        count_ls.append(function_name(number))
    score = int(np.mean(count_ls))
    print(f"Your algorithm can guess a number in {score} attempts.")
    return (score)

score_game(binary_search_guess_a_number)
