def pattern(n):
    for i in range(1,n+1):
        print("*"*i)



def oddeven (a):
    if a%2==0:
        print("a is even number")
    else:
        print("a is odd number")


def maxoftwo(a,b):
    if a>b:
        print("a is greter number")
    else:
        print("b is greter number")



def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print("a is greter number")
        else:
            print("c is greter number")
    elif b>c:
        print("b is greter number")
    else:
        print("c is greter number")


def fibonaci(n):
    a,b=0,1
    while b<n:
        print(b,end='')
        a,b=b,a+b



def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%2==0:
                print("n is not prime number")
                break
        else:
                print("n is prime number")
    else:
        print("n is not prime")
prime(21)        
        
