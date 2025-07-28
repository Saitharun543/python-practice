# l=[1,2,3,4]
# c=[i*i for i in l]
# print(c)

# l=[3,2,6,4,5]
# c=[i for i in l if i%2==0]
# print(c)

# l=[1,2,3,4]
# li=[2,3,4,5,6,7]
# c={i:j for i,j in zip(l,li)}
# print(c)

# li=[2*i for i in range(1,11)]
# print(li)

# l=[2,3,4,5,6,7,1,8]
# li=[i**2 if i%2==0 else i**3 for i in l ]
# print(li)


# l=[1,2,3,4]
# li=[2,3,4,5]
# c=[i+j for i,j in zip(l,li)]
# print(c)

# l=eval(input("enter the value: "))
# li=eval(input("enter the value: "))
# c=[i+j for i,j in zip(l,li)]
# print(c)


# l=eval(input("enter the value: "))
# li=eval(input("enter the value: "))
# list1=[int(i) for i in l]
# list2=[int(i) for i in li]
# v=[list1[i]+list2[i] for i in range(len(list1))]
# print(v)


# l=["sql","python","web","java"]
# dic={l[i]:i for i in range(len(l))}
# print(dic)

# l=["sql","python","web","java"]
# dic={i[0]:i for i in l if len(i)%2==0}
# print(dic)


# l=["king","mom","dad","lion","madam"]
# li={i:i if i=i[::-1] else  for i in range(len(l))}
# print(li)


# s=[1,2,3,3,4,5,5,6,7,9]
# set={i for i in s}
# print(set)

# def multiplication(a,b):
#     return a*b
# m=multiplication(10,20)
# print(m)

# def sum(a,b):
#     print(a+b)
# sum(10,20)

# def palindrome(name):
#     if name==name[::-1]:
#         print("given string is palindrome")
#     else:
#         print("given string is not a palindrome") 
# palindrome("mom")           


def num(a,b):
    if a>=b:
        return "true"
    else:
        return "false"
r=num(10,20)
print(r)
