#! python3
# BulletPointAdder.py - Adds Wikipedia bullt points to the start
# of each line of text in the clipboard.


import pyperclip
text = pyperclip.paste()

# Seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = f'* {lines[i]}'
text = '\n'.join(lines)
pyperclip.copy(text)
