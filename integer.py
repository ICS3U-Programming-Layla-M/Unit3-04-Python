#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May, 12, 2021
# This program asks the user to input a number whole number
# and then displays whether it's positive, negative or zero

def main():
    # ask the user to input a number
    number = int(input("Enter a whole number: "))

    # checks and displays if number is positive, negative or zero
    if (number > 0):
        print("{} is a positive number.". format(number))
    elif (number < 0):
        print("{} is a negative number.". format(number))
    else:
        print("{} is just zero!". format(number))


if __name__ == "__main__":
    main()
