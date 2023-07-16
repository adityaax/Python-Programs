myBoard =  { 'top-L':'' , 'top-M':'' , 'top-R':''  ,
                 'mid-L':'' , 'mid-M':'' , 'mid-R':''  ,
                 'bottom-L':'' , 'bottom-M':'' , 'bottom-R':'' }

def ticPrint():
    print(myBoard['top-L'],myBoard['top-M'],myBoard['top-R'])
    print(myBoard['mid-L'],myBoard['mid-M'],myBoard['mid-R'])
    print(myBoard['bottom-L'],myBoard['bottom-M'],myBoard['bottom-R'])

def gameBegin():
    player = 'X'
    print('There are two player- X and O')
    ticPrint()
    for i in range(9):
        print('It is the chance of {}'.format(player))
        print('Which field you want to fill? eg. top-L,bottom-M etc.,')
        ch = input('Enter your choice')
        if player == 'X':
            myBoard[ch] = 'X'
            player = 'O'
        else:
            myBoard[ch] = 'O'
            player = 'X'
        ticPrint()

gameBegin()
