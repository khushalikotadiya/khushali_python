import kk

while True:
    print("1. pattern")
    print("2. oddeven")
    print("3. maxoftwo")
    print("4. maxofthree")
    print("5. fibonaci")
    print("6. prime")
    print("7. exit")


    c=int(input("enter your choice:"))



    if c==1:
        n=int(input("enter value:"))
        kk.pattern(n)

    elif c==2:
        a=int(input("enter value:"))
        kk.oddeven(a)

    elif c==3:
        a=int(input("enter value:"))
        b=int(input("enter value:"))
        kk.maxoftwo(a,b)

    elif c==4:
        a=int(input("enter value:"))
        b=int(input("enter value:"))
        c=int(input("enter value:"))
        kk.maxofthree(a,b,c)

    elif c==5:
        n=int(input("enter valur:"))
        kk.fibonaci(n)

    elif c==6:
         n=int(input("enter valur:"))
         kk.prime(n)

    else:
        break 
        
        
        
          
