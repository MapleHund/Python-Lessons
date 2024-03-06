# Write your code here :-)
def count(s):
    syllables = 1
    for i in s:
        if i=='-':
            syllables += 1
    return syllables

print(count('hel-lo'))
