'''for i in range(10,0,-1):
    print(i)'''


'''i=10
while i>0:
    print(i)
    i-=1  '''

'''a=2145
c=0
while a>0:
    a//=10
    c+=1
print(c)  '''

# n=111
# temp=n
# reverse=0
# while n>0:
#     r=n%10
#     reverse=reverse*10+r  
#     n=n//10                          #in a given programing after reversing leading zeroes will not store
# if reverse==temp:
#     print(f"it is a palindrom")
# else:
#     print(f"it is not a palindrom")  


'''a=[0,1,2,3]
for a[-1] in a:
    print(a[-1])'''

# a=153
# t=a
# temp=a
# sum=0
# c=0
# while a>0:
#     a//=10
#     c+=1
# while t>0:
#     rem=t%10
#     sum=sum+rem**c
#     t=t//10
# if temp==sum:
#     print(f"{sum} is armstrong")
# else:
#     print(f"{sum} is not armstrong")


# for i in range(1,200):
#     sum=0
#     a=i
#     c=len(str(a))
#     while a>0:
#       rem=a%10
#       sum=sum+rem**c
#       a=a//10
#     if i==sum:
#        print(f"{i} is a armstrong number")

# a=6
# sum=0
# for i in range(1,a):
#     if a%i==0:
#         sum=sum+i
# if sum==a:
#     print(f"{a} is a perfect number")
# else:
#     print(f"{a} is not a perfect number") 



# a=1634
# t=a
# temp=a
# sum=0
# c=0
# while a>0:
#     a//=10
#     c+=1
# while t>0:
#     rem=t%10
#     sum=sum+rem**c
#     t=t//10
# if temp==sum:
#     print(f"{sum} is armstrong")
# else:
#     print(f"{sum} is not armstrong")

# a=int(input("enter a value: "))
# for i in range(1,10):
#     if i*i==a:
#         print(f"{a} is a perfect square")
#         break
# else:
#     print(f"{a} is not a perfect square")


# a=int(input("enter a value: "))
# sum=0
# for i in range(1,10):
#     sum=a+1
#     if i*i==sum:
#         print(f"{a} is a sunny number")
# else:
#     print(f"{a} is not a sunny number")        


# a=int(input("enter a value:"))
# s=a*a
# sum=0
# while s!=0:
#     rem=s%10
#     sum=sum+rem
#     s=s//10
# if a==sum:
#     print(f"{a} is a neon number")  
# else:
#     print(f"{a} is not a neon number")

# n=5
# a1=0
# a2=1
# sum=0
# for i in range(1,n+1):
#     print(sum,end=" ")
#     a1=a2
#     a2=sum
#     sum=a1+a2

# li=[1,2,3,1,2,4,5,3,4,6,5]
# l=[]
# for i in li:
#     if i not in l:
#         l+=[i]
# print(l)     


# li=[1,2,3,1,4,3]
# l=[]
# for i in li:
#     if i not in l:
#         l+=[i]
# print(l)     


# s="today is wednesday"
# w=s.split()
# w1={}
# for i in w:
#     w1[i]=i[::-1]
# print(w1)    
    
# s = "today is wednesday"
# words = []
# word = ""
# index_word_dict = {}
# index = 0
# for char in s:
#     if char != ' ':
#         word += char
#     else:
#         if word:
#             words.append(word)
#             word = ""
# if word:
#     words.append(word)
# i = 0
# while i < len(words):
#     index_word_dict[i] = words[i]
#     i += 1
# print(index_word_dict)

    
# l=[1,2,3,4]
# li=l[::-1]
# print(li)

# l=[2,3,1,4]
# li=[]
# c=len(l)-1                          #reversing the list using for loop
# for i in range(c,-1,-1):
#     li=li+[l[i]]
# print(li)    


#BUBBLE SORT
# a=[2,6,8,3,1]
# c=len(a)-1
# for i in range(0,c):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)


# a=[1,2,3,4,5]
# l=max(a)
# print(l)


# a=[2,6,3,8,1]
# m=0
# for i in a:
#     if m<i:
#         m=i
# m1=0
# for j in a:
#     if j>m1 and j!=m:
#         m1=j
# print(m1)        

# n=input("enter a string: ")
# a=n.count("o")
# print(a)

# s="pyspiders"
# char="p"
# c=0
# for i in s:
#     if i==char:
#         c+=1
# print(c)        

# s="pyspiders"
# u=""
# d=""
# for i in s:
#     if i in u and i not in d:
#         d=d+i
#     else:
#         u=u+i
# print(d)              


# l=[2,7,4,11,10]
# sum=9
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==sum:
#             print(i,j)

# s=4
# for i in range(s):
#     print("*",end="")

# s=4
# d=4
# for i in range(s):
#     for j in range(d):
#         print("a",end=" ")
#     print()    

# a=int(input("enter a value: "))
# for i in range(a):
#     print("*",)


# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()   


# n=int(input("enter a value:"))
# for i in range(n):
#     print("*"*(n-i))

# for i in range(6,0,-1):  
#     for j in range(i):                        #inverted triangle
#         print("*", end=" ")
#     print()


n = 4
for i in range(1, n + 1):
     print(" " * (n - i),end="")         #triangle
     for j in range(i):
        print("*",end=" ")
     print()


# n=4
# for i in range(n):                         #triangle
#     print(" "*(n-i-1)+f"{i+1} "*(i+1))


n = 4
for i in range(n, 0, -1):  
    print(" " * (n - i), end="")          
    for j in range(i):
        print(chr(65+j), end=" ")
    print()



n=3
for i in range(n):
    print("* "*(i+1))
for i in range(n):
    print("* "*(n-i-1))    


n=3
for i in range(n):
    print("  "*(n-i-1)+"* "*(i+1))
for i in range(n):
    print("  "*(i+1)+"* "*(n-i-1)) 