'''
write a pythone program to get the fibonacci series of given range.
'''

n=int(input("enter N:"))
a,b=0,1
while b<n:
    print(b,end="")
    a,b=b,a+b
