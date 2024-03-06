# the get() method
picnicItems = {'apples': 5, 'cups': 2}
spam = 'zero'

print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.','\n')
# The get() arguments return the retrieved value
# from the dictionary or uses a fallback

print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.','\n')
# 'eggs' is not in dictionary output is fallback

print('I am bringing ' + str(picnicItems.get('eggs')) + ' eggs.','\n')
# with no fallback, the None value is used

print('I am bringing ' + str(picnicItems.get('eggs', 0.0)) + ' eggs.','\n')
# The fallback can be a float

print('I am bringing ' + str(picnicItems.get('eggs', 'no')) + ' eggs.','\n')
# a string

print('I am bringing ' + str(picnicItems.get('eggs', spam)) + ' eggs.','\n')
# Or even a variable!

print('I am bringing ' + str(picnicItems.get()) + ' eggs.','\n')
# An error, obviously, if no arguments are given
