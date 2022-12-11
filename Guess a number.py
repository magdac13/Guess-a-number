import random


def guess():
    """Function defines if user guessed a number chosen by a computer (from range 1 to 100)"""

    correct_answer = random.randint(1, 100)
    while True:
        try:
            n = int(input("Guess a number: "))
            break
        except ValueError:
            print("It's not a number!")
    if n < correct_answer:
        print("Too small!")
    elif n > correct_answer:
        print("Too big!")
    elif n == correct_answer:
        return "You win!"

    return guess()


print(guess())