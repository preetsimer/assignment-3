#question 1
n=int(input("Enter size of list "))
l=[]
print("Enter list elements ")
for i in range(1,n+1):
    a=input()
    l.append(a)
print(l)
#question 2
print("Merged List ")
l2=["google","apple","facebook","microsoft","tesla"]
l=l+l2
print(l)
#question 3
e=input("Enter element to account its occurrence :")
c=l.count(e)
print(c)
#question 4
n=int(input("Enter size of list "))
l=[]
print("Enter list elements ")
for i in range(1,n+1):
    a=input()
    l.append(a)
l.sort()
print("The sorted list is ")
print(l)
#question 5
a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[]
c=a+b
c.sort()
print(c)
#question 6
n=int(input("Enter size of list "))
l=[]
print("Enter list elements ")
for i in range(1,n+1):
    a=int(input())
    l.append(a)
odd=0
even=0
for i in range(0,n):
    if (l[i]%2)==0:
        even=even+1
    else:
        odd=odd+1
print("there are %s even elements in list"%even)
print("there are %s odd elements in list"%odd)
#Tuples
#question 1
t=(1,2,3,4,5)
a=reversed(t)
print(tuple(a))
#question 2
t=(1,2,3,4,5)
print("max element in a tuple is ",max(t))
print("max element in a tuple is ",min(t))
#Strings
#question 1
st=input("Enter a string to convert it into upper case ")
print(st.upper())
#question 2
st=input("Enter a string ")
if st.isdigit():
    print("true")
else:
    print("false")
    
#question 3
s="Hello World"
print(s.replace("World","Simer"))
    










        




    
      
