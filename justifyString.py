import sys
#! python3
# justifyString.py - usage of justify method of string eg., rjust(), ljust(), center()

tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]


k=0
count=0
def printData(listD):
    global count
    global k
    if count>=4:
        sys.exit()
    for i in range(len(listD)):
        print(listD[i][k].center(10,'*'),end=' ')
    print()
    k+=1
    count+=1
    printData(listD)


printData(tableData)
