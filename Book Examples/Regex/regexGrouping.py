import re

phoneNumRegex  = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo =  phoneNumRegex.search('My number is 415-555-4242.')

print(mo.group(1),'\n')

print(mo.group(2),'\n')

print(mo.group(),'\n')

# groups() return a tuple of multiple values
print(mo.groups(),'\n')
areaCode, mainNumber = mo.groups()

print(areaCode, '\n')

print(mainNumber, '\n')
