# partition() method


# Returns a tuple seperated at the passed string.
print('Hello, world!'.partition('w'),'\n')

print('Hello, world!'.partition('world'),'\n')

# only splits at the first found instance.
print('Hello, world!'.partition('o'),'\n')

# returns the entire string as the first value
# if the passed string is not found.
print('Hello, world!'.partition('XYZ'),'\n')

# Multiple assignment trick can be used for the returned strings
before, sep, after = 'Hello, world!'.partition(', ')
print(f'{before}\n{sep}\n{after}')
