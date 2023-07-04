# inventory.py
# Fantasy game inventory from Chapter 5, Automate the boring stuff with python
#
# James // rqvl@runbox.com

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += inventory.get(k,0)
        print(v,k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)