
'''

write a python program to add 'ing' at the end of a given string (length should be at least 3). if the given string already ends with 'ing' then add 'ly'
instead if the string length of the given string is less than 3, leave it unchanged.

'''



v1="cut"
if len(v1)>=3:
    if v1[-3:]=="ing":
       v1 =v1+"ly"
    else:
        v1=v1+"ing"
        print(v1)
else:
    print(v1)
        
