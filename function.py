from operator import ne


def addTwo(x,y):
    z=x+y
    return z

# a=addTwo
# print(a(2,3))

print(addTwo(2,3))
#Arbitrary Arguments, *args

def my_function(*kids):
    print("The youngest child name is:",kids[2])

my_function("emil","temil","kemil")


#Keyword Arguments

def new_function(child2,child1,child3):
    print("Name of child-1 is :",child1)

new_function(child2 = "Tobias",child3 = "Linus",child1 = "Emil",)


#Arbitrary Keyword Arguments, **kwargs

def full_name(**name):
    fname=name['fname']
    lname=name['lname']
    print(f"Your name is:{fname} {lname}")

full_name(fname = "Tobias", lname = "Refsnes")


#To handle errors Default Parameter Value

def subtract_two(a,b=0):
    c=a-b
    return c

print(subtract_two(6,4))
print('\n')

def func(required_arg, *args, **kwargs):
    # required_arg is a positional-only parameter.
    print(required_arg)

    # args is a tuple of positional arguments,
    # because the parameter name has * prepended.
    if args: # If args is not empty.
        print(args)

    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended.
    if kwargs: # If kwargs is not empty.if emty it return none not error
        print(kwargs)

func("required argument")
print('\n')
func("required argument", 1, 2, '3')
print('\n')
func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")