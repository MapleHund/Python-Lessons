# Listing from a distionary, and adding new itmes to a dictionary from a list
#
# Revisit this one later to improve it

playerInventory = {'Torches':2, 'Daggers':1, 'Health potions':5, 'Gold':10}
loot = ['Sword','Diamond','Gold']


# Prints a list of all items in the inventory dictionary, then lists total count of items.
def displayInventory(playerInventory):
    print('Inventory contains:')
    totalItems = 0

    for invItem,invItemCount in playerInventory.items():
        print(str(invItemCount) + ' ' + str(invItem))
        totalItems += invItemCount

    print('Total items in inventory is: ' + str(totalItems))

# Adds all items in the loot list to the inventory dictionary
def addToInventory(playerInventory, lootedItems):
    print('Items added to inventory:')
    for item in lootedItems:
        if item in playerInventory:
            playerInventory[item] += 1
        else:
            playerInventory[item] = 1
    print(str(loot))


displayInventory(playerInventory)
print()
addToInventory(playerInventory, loot)
print()
displayInventory(playerInventory)
