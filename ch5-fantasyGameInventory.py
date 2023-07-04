# inventory.py
# Fantasy game inventory from Chapter 5, Automate the boring stuff with python
#
# James // rqvl@runbox.com

import copy

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    inventory = copy.copy(inventory) 
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += inventory.get(k,0)
        print(v,k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff) # first part of problem
print()
inv = addToInventory(inv, dragonLoot) 
displayInventory(inv) # list-to-dict
