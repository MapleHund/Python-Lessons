import locale
locale.setlocale(locale.LC_ALL, 'en_US')
print(locale.getlocale())

print('%s, eggs, and %s' % ('spam', 'Spam!'))

print('{0} and {1}'.format('cats', 'dogs'))

print('{} and {}'.format('eggs', 'bacon'))

print('{:n}'.format(237331.35456))