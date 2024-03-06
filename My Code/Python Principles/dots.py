def add_dots(s):
    return '.'.join(s)

def remove_dots(s):
    return s.replace('.','')

print(remove_dots(add_dots('hello')))
