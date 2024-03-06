sillyAnimalPeople = {'Tachi':'weasel', 'Meeka':'Mouse', 'Adeon':'Fox'}


while True:
    print('Type the name of a friend:    (\'Q\' to exit)')
    name = input()
    print()

    if name.lower() == 'q':
        break
    elif name == '':
        continue
    # Check if name is already in dectionary, if True print out name and value
    if name in sillyAnimalPeople:
        print(name + ' is a ' + sillyAnimalPeople[name] + '.','\n')
        continue

    # If name is not found, prompt to add
    print(f'{name.title()} not found.')
    print(f'What is this {name.title()}\'s species?')
    species=input()
    if species.lower() == 'q':
        break
    elif species == '':
        continue
    sillyAnimalPeople[name] = species # Name and species is added to dictionary
    print(f'{name} added\n')
