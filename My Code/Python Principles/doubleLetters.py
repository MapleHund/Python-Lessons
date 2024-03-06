def double_letters(string):
    last_letter = ''
    for i,v in enumerate(string):
        cur_letter = v
        if last_letter == cur_letter:
            return True
        last_letter = cur_letter
    return False

print(double_letters('abccde'))
