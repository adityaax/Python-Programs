import random
print("I selected a number between 1-20 both including, your task is to guess my number-\n")
print("You have only 6 attempts\n")
myNum=random.randint(1,20)
for num in range(1,7):
    print("This is your {} attempt".format(num))
    try:
        userNum=int(input("Enter the number- "))
        if myNum<userNum:
            print('Your number is greater than my :(\n')
        elif myNum>userNum:
            print('Your number is less than my :(\n')
        else:
            print(':) You guess the correct number in '+str(num)+' attempts :)')
            break
    except ValueError:
        print("Is the value you provided is integer value?")

