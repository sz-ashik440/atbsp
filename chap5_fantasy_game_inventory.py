stuff = {'rope': 1, 'tourch': 6, 'gold coin': 42, 'dagger': 1, 'arrow':12}

def displayInventory(inventory):
    print('Inventory')
    totalItem = 0
    for k,v in inventory.items():
        print(str(v)+' '+k)
        totalItem+=v

    print('Total Number of items: '+ str(totalItem))

displayInventory(stuff)
