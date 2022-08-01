'''
write a python program to get the fectorial number of given number.
'''


n=int(input("enter N:"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print("factorial:",fact)    
