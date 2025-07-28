'''name="manish"
age=25
print("your anme is:,age is:",name,age)
print(f"your anme is{name}:,age is:{age}")
'''
'''name=input("enter your name: ")
age=input("enter your age:")
print(f"my name is:{name},age is:{age}")
print("my name is {} and age is {}".format(name,age))    #we can pass either empty braces or index values also loke given below
print("my name is {0} and age is {1}".format(name,age))
print("my name is "+name+" and age is "+age)                #this is the concatenation by using '+' operator'''

'''a=10
b=5
if a>b:
    print("a is greater than b")
print("outside if block") ''' 

'''a=10
b=50
if a>b:
    print("a is greater than b")
print("outside if block")   '''

'''a=input("enter a number: ")
b=input("enter a number: ")
if a>b:
    print("a greater than b")
print("outside if block")    '''

'''a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a>b:
    print("a greater than b")
print("outside if block")   ''' 

'''name="kavya"
if name=="navya":
    print(f"name is {name}")
print("outside the if block")    

a="python"
if "m" in a:
    print("a in python")
print("outside the if block")

l=[1,2,3,4]
if 5 not in l:
    print("5 is not in list")
print("outside the if block")


e=10
f=10
if e is f:
    print("e and f are same objects")
print("outside the if block")


g=10
h=10.0
if g is not h:
    print("g and h are not same objects")
print("ouside the if block")

a=10
b=25
c=27
if a<b<c!=a:
    print("a is less than b and b is less than c and c is not equal to a")
'''


'''a=10
b=5
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is not greater than {b}")'''


'''e=10
f=50
if e>f:
    print(f"{e} is greater than {f}")
else:
    print(f"{e} is not greater than {f}")        



a=10
if a>0:
    print(f"{a} is a positive number")
elif a<0:
    print(f"{a} is a negative number")
else:
    print(f"{a} is zero")          '''


'''a="python"
if "m" in a:
    print(f"m in {a}")
elif "i" in a:
    print(f"o in {a}")
else:
    print("both are not present") 


b="python"
if "m" in b:
    print(f"m in {b}")
elif "n" in b:
    print(f"o in {b}")
else:
    print("both are not present")       '''

'''a=10
if a>0:
    if a>5:
        print(f"{a} is greater than 5")
    else:
        print(f"{a} is not greater than 5")
else:
    print(f"{a} is not grater than 0 ") '''


a=10
if a>0:
    if a>5:
        print(f"{a} is greater than 5")
    else:
        print(f"{a} is not greater than 5")    
else:
    print(f"{a} is not greater than 0 ") 


b=-10
if a>0:
    if b>5:
        print(f"{b} is greater than 5")
    else:
        print(f"{b} is not greater than 5")    
else:
    print(f"{b} is not greater than 0 ")     


e=int(input("enter a number: "))                               
f=int(input("enter a number: "))
g=int(input("enter a number: "))
if e>f:
    if f>g:
        print(f"{f} is greater than {g}")
    else:
        print(f"{f} is not greater than {g}") 
else:
    print(f"{e} is not greater than {g}")           

     






