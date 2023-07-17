inventory = {'rope':1,'torch':6,'gold coin':42,'dagger':1,
             'arrow':12}
'''
def displayInventory(inventory):
    print('Your inventory- ')
    tot=0
    for k,v in inventory.items():
        print(v,' ',k)
        tot+=v
    print('Total number of items- ',tot)

displayInventory(inventory)
'''

def newInventory(old,new):
    for dr in new:
        old.setdefault(dr,0)
        for inv in old.keys():
                if dr==inv:
                    old[inv]+=1
        
    print(old)
dragonLoot=['ruby','gold coin','ruby','gold coin','gold coin','dagger']
newInventory(inventory,dragonLoot)
