from pathlib import Path
import os
p = Path('G:/Python Lessons')

p.glob('*')

print(list(p.glob('*'))) # Make a list from the generator.
print()
print(list(p.glob('*.txt'))) # Lists all text files.
print()
list(p.glob('*.?x?')) # ? serves as a character wildcard
