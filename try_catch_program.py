#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program asks user to pick a number from 0-9
# and tells them if they got it right or wrong


import random

random = random.randint(1, 9)


def main():
    # This function makes the user guess a number from 0-9

    # input
    number = input("Guess my number (0-9): ")
    print("")

    # process
    try:
        integer = int(number)
        if int(number) == random:
            # output
            print("Correct!")

        else:
            print("Wrong! Correct number is:{} ".format(random))

    except ValueError:
        print("Please place an integer next time")

    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
