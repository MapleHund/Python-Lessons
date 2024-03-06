itemList = []
def readList(l):
    for index, item in enumerate(l):
        print(item + ', ' if index != len(l) - 1 else 'and ' + item,end='')
    print()
def askList(l):
    while True:
        print('enter an item:')
        i = input()
        if i == '':
            break
        else:
            l.append(i)


askList(itemList)
readList(itemList)
