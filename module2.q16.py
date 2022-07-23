'''
write a python program to count the occurences of each word in a given sentence.

'''

str=input("enter line of string")
str=str.split()
i=0
count=0
while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count=count+1
    print(str[i],"present",count,"times")
    i=i+1
