# coin flips
import random
streakCurrent = 0
streakHighest=  0
currentFlip = ''
lastFlip = ''
for i in range(100):
    currentFlip = random.randint(1,2)
    print('H' if currentFlip == 1 else 'T')
    if currentFlip == lastFlip:
        streakCurrent += 1
    else:
        lastFlip = currentFlip
        if streakCurrent >= streakHighest:
            streakHighest = streakCurrent
            streakCurrent = 0
print('Highest streak was ' + str(streakHighest + 1))
