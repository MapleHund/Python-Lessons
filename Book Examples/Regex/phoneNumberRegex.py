import re

# Variable is assigned the regex object. \d means a digit.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


# call regex search on compiled pattern with a string
mo = phoneNumRegex.search('my number is 415-555-4242.')


print(f'phone number found {mo.group()}\n')

print('Input string')
eggs = str(input())

# re.search(pattern, string, flags=0)
# The pattern can be defined in the search
# along with what string to search
# \s is a space
spam = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', eggs)

print(spam.group())
