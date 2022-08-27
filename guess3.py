#Guess 3-digit number -
'''
output is 'close' - If one digit is correct but not at correct position 
output is 'closeto' - If one digit is correct and at last position
putput is 'try' - No digit is correct
You have 10 attempts
'''

number='783'
def more():
    guess()

def guess():
    i=1
    while i<=11:
        if i>10:
            q=input('chances over :() want to play again y/n : ')
            if q=='y':
                more()
            else:
                print('exit')

        num=input('Guess 3 digit number - ')
        if len(num)<3 or len(num)>3:
            print('! Only 3 digit number is allowed !')
            print('Play again -> ')
            more()
        elif num==number:
            print('Jai Ho Mil Gya :) Number - {} '.format(num))
            m=input('Want to play again y/n - ')
            if m=='y':
                more()
            else:
                print('exit')
        elif (num[0]==number[0] or num[0]==number[1] or num[0]==number[2]) or (num[1]==number[0] or num[1]==number[1] or num[1]==number[2]):
            print('close')
            i+=1
        elif (num[2]==number[2]):
            print('closeto')
            i+=1
        else:
            print('try')
            i+=1
guess()
