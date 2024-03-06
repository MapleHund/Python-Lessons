def spam():
    print(ham)
    global eggs
    eggs = 10

eggs = 20
print(eggs)
ham = eggs
spam()
print(eggs)
