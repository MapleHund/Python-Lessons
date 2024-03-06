bottles = 99
decend = True
def word(i):
    if i == 1 or 0:
        return ' bottle '
    else:
        return ' bottles '

def song(i, o):
    print(str(i) + word(i) + 'of beer on the wall. ' + str(i) + word(i) + 'of beer. ')
    print('Take one down, pass it around')
    if o == true:
        i -= 1
    else:
        i += 1
    print(str(i) + word(i) + 'of beer on the wall.')
    print()
    if i == 0:
        o = False
    elif i == bottles:
        o = True
    song(i, o)
song(bottles, decend)
