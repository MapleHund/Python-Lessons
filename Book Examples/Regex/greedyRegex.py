import re

haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('HaHaHaHa')
print(mo1.group())
