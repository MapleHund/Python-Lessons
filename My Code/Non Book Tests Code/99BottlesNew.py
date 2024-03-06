bottles = 99

def addS():
    print('s', end='')

while bottles > 0:
    print(str(bottles) + ' bottle', end='')
    if bottles != 1:
        addS()
    print(' of beer on the wall ' + str(bottles) + ' bottle', end='')
    if bottles != 1:
        addS()
    print(' of beer.')

    print('Take one down, pass it around')
    bottles = bottles - 1
    print(str(bottles) + ' bottle', end='')
    if bottles != 1:
        addS()
    print(' of beer on the wall.')
    print()
