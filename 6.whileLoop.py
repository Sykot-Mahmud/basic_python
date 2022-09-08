loop=True

while loop:
    name=input("Enter a  name\n")
    print("You Enter: ",name)

    if name=='stop':
        print("Break the loop")
        loop=False # can use break 
        