# join() and split() methiods for strings
spam = ['cats', 'rats', 'bats']
eggs = ['My', 'name', 'is', 'simon']
ham = 'My name is simon'

# join() is called on what it inserts
print(', '.join(spam),'\n')

print(''.join(spam),'\n')

print(' '.join(eggs),'\n')

print('ABC'.join(eggs),'\n')

print(ham.split(),'\n')

print(ham.split('m'),'\n')

