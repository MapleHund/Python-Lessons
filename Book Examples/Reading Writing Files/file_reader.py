from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

# print(pi_string)
# print(len(pi_string))

birthday = input('enter your birthday as ddmmyyyy: ')
if birthday in pi_string:
    print('birthday found')
else:
    print('birthday not found')
