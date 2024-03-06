# Repating Collatz checker
# repats 3n+1 starting at 1
# records longest sequence
def collatz(i):
    if i % 2:
        return int(3 * i + 1)
    return int(i / 2)

curNum = 0
curLen = 0
longestSeqDict = {'':[]}
def storeFinalSeqLenth(startNum, curLen):
    if curLen in longestSeqDict.key():
        longestSeqDict().append

print('Enter number to run sequence to:')
cap = int(input())
print(f'Running 3n+1 up to a starting number of {cap}')
for startNum in range(1, cap + 1):
    curNum = startNum
    curLen += 1
    while curNum != 1:
        curNum = collatz(curNum)
        curLen += 1
    storeFinalSeqLenth(startNum, curLen)


print('Program Complete\n')
print(f'The longest was {longestSequence[0]}\
, with a {len(longestSequence)} long sequence.')
