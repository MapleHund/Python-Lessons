# Collatz Conjecture
import sys, time
def collatz(i): # get next number in sequence
    if i % 2 == 0:
        return int(i / 2)
    else:
        return int(i * 3 + 1)


def askForNumber(number): # function to ask for number
    try:
        print('Enter a number:')
#        number = int(input())
#        number = input()
#        number = int(number)
        if number == 0: # Reject 0
            print('Invalid Number')
            return askForNumber(2)
        else:
            return askForNumber(number - 1)
    except ValueError: # Error handling for anything but a number
        print('You must enter a number.')
        return askForNumber(5)

number = askForNumber(8)
while True: # Keep running until sequence reaches 1
    time.sleep(0.1)
    if number != 1:
        number = collatz(number)
        print(number)
    else:
        print(number)
        number = askForNumber(8)

