#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def function():
    print("I am Function")

# TODO: function that takes arguments
def function2(x,y):
    print(x," ", y)

# TODO: function that returns a value
def cube(x):
    return x*x*x 

# TODO: function with default value for an argument
def function3(arg, x=1):
    result = 1
    for _ in range(x):
        result = result * arg
    return result 

# TODO: function with variable number of arguments
def function4(*args):
    result = 0
    for x in args:
        result = result + x
    return result 


# function()
# print(function())
# print(function)

# function2(2,3)
# print(function2(2,3))

#cube(3)
#print(cube(3))

#print(function3(2,3))

print(function4(2,3,4,5, 10))