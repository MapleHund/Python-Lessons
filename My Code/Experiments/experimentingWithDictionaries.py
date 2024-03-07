# Tests with dictionaries
ham = 'cat'
eggs = 'dog'
spam = {'a':'1','b':'2', 'c':'3', 'd':eggs} # eggs becomes the string in eggs. Why?
print('ham variable is ' + str(ham))
print('spam dictionary is ' + str(spam))
print()

spam['b'] = ham
print(spam)
print()

ham ='bird'
eggs = 'fox'
print('ham is now ' + str(ham) + ', eggs is now ' + str(eggs))
print(spam)





