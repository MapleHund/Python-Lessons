# Collatz Conjecture
import sys, time
def collatz(i): # get next number in sequence
    if i % 2 == 0:
        return int(i / 2)
    else:
        return int(i * 3 + 1)


def askForNumber(): # function to ask for number
    try:
        print('Enter a number:')
        number = int(float(input()))
#        number = input()
#        number = int(number)
        if number <= 0: # Reject 0 and negative numbers
            print('Invalid Number')
            return askForNumber()
        else:
            return number
    except ValueError: # Error handling for anything but a number
        print('You must enter a number.')
        return askForNumber()

number = askForNumber()
sequence = 1
while True: # Keep running until sequence reaches 1
#    time.sleep(0.1)
    print(f'{sequence}: {number}')
    sequence += 1
    if number != 1:
        number = collatz(number)
    else:
        number = askForNumber()

