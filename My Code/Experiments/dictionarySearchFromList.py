#Using a list to search for matches in a dictionary

spam={'cat':1,'bat':2,'rat':3}
eggs=['rat','bear','3',1,('bat',2)]

print('key search')
for i in eggs:
    print(i in spam.keys())     # This will output 'True False False False False'
                                # becasue this search looks for matching keys

print()
print('value search')
for i in eggs:
    print(i in spam.values())   # This will output 'False False False True False'
                                # becasue this search looks for matching values

print()
print('item search')
for i in eggs:
    print(i in spam.items())    # This will output 'False False False False True'
                                # becasue this search looks for matching key-value pairs

print()
print('key search')
for i in eggs:
    print(i in spam)            # This will output 'True False False False'
                                # becasue this search looks for matching values
