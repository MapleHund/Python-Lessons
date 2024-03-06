bottles = 99
while bottles > 0:
    if bottles != 1:
        print(str(bottles) + ' bottles of beer on the wall. ' + str(bottles) + ' bottles of beer.' )
        print('Take one down. Pass it around.' )
        bottles -= 1
        print(str(bottles) + ' bottles of beer on the wall.')
        print()

    else:
        print(str(bottles) + ' bottle of beer on the wall. ' + str(bottles) + ' bottle of beer.' )
        print('Take one down. Pass it around.' )
        bottles -= 1
        print(str(bottles) + ' bottles of beer on the wall.')
        print()
