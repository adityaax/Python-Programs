dictPicnic = { 'Ajay':{'Apple':2,'Orange':5,'Banana':6},
               'Ravi':{'Sandwich':6,'Banana':3,'Burger':6},
               'Sarthak':{'Apple':5,'Orange':5,'Sandwich':6}}

def countItem(dictP,item):
    c=0
    for k,v in dictPicnic.items():
        c+=v.get(item,0)
    return c

print('Total apples are- ',countItem(dictPicnic,'Apple'))
print('Total oranges are- ',countItem(dictPicnic,'Orange'))
print('Total bananas are- ',countItem(dictPicnic,'Banana'))
print('Total sandwich are- ',countItem(dictPicnic,'Sandwich'))
print('Total burgers are- ',countItem(dictPicnic,'Burger'))
