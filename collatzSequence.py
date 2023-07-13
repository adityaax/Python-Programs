#The Collatz Sequence is one of the most famous unsolved problems in mathematics. Search about it
def even(number):
    if number%2==0:
        return True
    
def collatz(number):
    n=number
    global nam
    if even(n):
        print(n//2)
        nam=n//2
    else:
        print(3*n+1)
        nam=3*n+1

nam=int(input("Enter any integer- "))
while nam!=1:
    collatz(nam)
