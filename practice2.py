rno=int(input("enter roll no:"))
sname=input("enter student name:")
s1=int(input("enter marks of student 1:"))
s2=int(input("enter marks of student 2:"))
s3=int(input("enter marks of student 3:"))
total=s1+s2+s3
per=total/3
print("roll no:",rno)
print("student name :",sname)
print("total:",total)
print("percentage:",per)
if per>=70:
    print("distanction")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
elif per>=40:
    print("pass")
else:
    print("fail")
