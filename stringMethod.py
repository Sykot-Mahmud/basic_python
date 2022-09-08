#strip,split,len,lower,upper

text=input("Enter a text\n")
print(len(text))
print(text.strip())

text1='hello.tim.bye'
print(text1.split('.'))

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
print(type(x))
