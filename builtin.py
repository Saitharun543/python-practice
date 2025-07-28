a="python"
result=a.upper()
print(result)

a="PYTHON IS EASY"
print(a.lower())
print(a.swapcase())
print(a.title())
print(a.capitalize())
print(a.count("P"))
print(a.count("Y",0)) #THE GIVEN NUMBER IS USED TO START FROM THE GIVEN SEQUENCE AND COUNT THE GIVEN ELEMENT

x="python from pyspiders"
print(x.index("p"))
print(x.rindex("s"))
print(x.rindex("p")) #rindex is known as reverse indexing,it fetches the index from reverse or lst value
print(x.index("p",2,19))
print(x.rindex("p",2,19)) # it is taking the index between 2 and 19 and giving the index of p  in the range from last
print(x.startswith("p"))
print(x.startswith("P"))
print(x.endswith("o"))
print(x.endswith("s"))
print(x.isalpha()) #because of space,if space is there in sequence isalpha shows the error
print(x.isalnum())
print(x.isupper())
print(x.islower())
print(x.find("p"))
print(x.find("l")) # if thr givrn substring is not present in the string we will gwt -1
print(x.split()) # if there is only on string is present in the sequence then it gives that single word in a list
print(x.replace("q","py")) # it is still immutable,we are just changing the character,but the address will remain same
print(x.strip()) # strip is used to remove the leading space means starting space
print(x.rstrip()) # rstrip is used to remove trailing space means ending space

y="python"
result="*".join(y)
print(result)

z="123"
print(z.isdigit())
print(z.isalnum())

n=" "
print(n.isspace())


