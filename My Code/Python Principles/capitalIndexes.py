eggs = []
def capital_indexes(spam):
    for i, letter in enumerate(spam):
        if letter.isupper():
            eggs.append(i)
    return eggs
