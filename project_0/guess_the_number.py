import sys
import numpy as np

LO_BORDER = 0  # constant, DO NOT reassign
HI_BORDER = 100  # constant, DO NOT reassign


# made for fun, could not be used for real testing
def manual_guess_the_number(number):
    attempts = 1
    print("Let's play a game. You should guess a secret number.")
    while True:
        guess = HI_BORDER
        try:
            value = input("Your guess:")
            if value == 'exit':
                sys.exit("Terminate the program.")
            guess = int(value)
        except ValueError:
            print("You are a dumb bitch. It's not a number.")
        if guess == number:
            print("Congratulations. You win. You did " + str(attempts) + " attempts.")
            break
        elif guess < number:
            print("Nope. The secret number should be bigger.")
        elif guess > number:
            print("Nope. The secret number should be less.")
        attempts += 1


def dumb_guess_the_number(number):
    # attempt to guess a random number using random
    # we generate a new random number each time
    attempts = 1
    while True:
        predict = np.random.randint(LO_BORDER, HI_BORDER)  # we generate a number between 1 and 100
        if number == predict:
            break
        attempts += 1
    return attempts


def incremental_guess_the_number(number):
    # attempt to guess a random number using incremental approach
    # we increase or decrease our number by 1
    attempts = 1
    predict = np.random.randint(LO_BORDER, HI_BORDER)  # we generate a number between 1 and 100
    while number != predict:
        attempts += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return attempts


def binary_search_guess_the_number(number):
    return binary_search_impl(number, LO_BORDER, HI_BORDER)


def binary_search_impl(number, lowest_range, highest_range):
    # attempt to guess a random number using binary search
    number = range_correction(number)
    lowest_range = range_correction(lowest_range)
    highest_range = range_correction(highest_range)
    # core logic
    attempts = 1
    predict = int((highest_range - lowest_range) / 2)
    while number != predict:
        attempts += 1
        if number > predict:
            lowest_range = predict
            predict = predict + int((highest_range - predict) / 2)
        elif number < predict:
            highest_range = predict
            predict = int((predict + lowest_range) / 2)
    return attempts


def range_correction(number):
    # validation
    if number > HI_BORDER:
        number = HI_BORDER
    elif number < LO_BORDER:
        number = LO_BORDER
    return number


def score_game(function_name):
    # run it n (> 1000) times, to find out how fast we could guess a number
    count_ls = []
    np.random.seed(1)  # setup RANDOM SEED, for science and repeatability
    random_array = np.random.randint(LO_BORDER, HI_BORDER, size=100000)
    for number in random_array:
        count_ls.append(function_name(number))
    score = int(np.mean(count_ls))
    print(f"Your algorithm can guess a number in {score} attempts.")
    return score


score_game(binary_search_guess_the_number)
