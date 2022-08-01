'''
write python program that swap two number with temp variable and without temp
variable .
'''

print("with temp")
x=int(input("enter x:"))
y=int(input("enter y:"))
temp=x
x=y
y=temp
print("x afterswap:",x)
print("y afterswap:",y)

print("without temp")
x=int(input("enter x:"))
y=int(input("enter y:"))
x,y=y,x
print("x after swap:",x)
print("y after swap:",y)
