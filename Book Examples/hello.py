# This program writes hello and asks for my name

print('hello world!')
print('What is your name?')
# input name
myName = input()
print('It is good to meet you,' + myName)
#Take length of name input, convert to string, Combine strings.
print('The length of your name is ' + str(len(myName)) + ' letters long.')
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

