#! python3
# bulletPointerAdder.py - adds bullet to list copied from clipboard
import pyperclip

result=pyperclip.paste()
splitListGet=result.split('\n')

for i in range(len(splitListGet)):
    splitListGet[i]='* '+splitListGet[i]
print('\n'.join(splitListGet))

# ! Copy these list to clipboard first !
list1=[1,2,3,4]
list2=[5,6,7,8]
list3=[9,10,11,12]
