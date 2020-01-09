#!/usr/bin/python3

# Function definition like C macro
sum = lambda a, b: a + b

def printSumWithLambda(a, b):
    "test of lambda function"
    print(sum(a, b))
    return

def argTypes(a, b, *var):
    print(a+b)
    print("Other vars:", end = ' ')
    for i in var:
        print(i)
    return

def defaultArg(a, b=20):
    print(a+b)
    return

printSumWithLambda(9, 5)

print("argTypes(x, y):", end = ' ')
argTypes(4, 5)
print("argTypes(x, y, z):", end = ' ')
argTypes(1, 3, "varssss")
print("defaultArgs(x, y): ", end = ' ')
defaultArg(4, 5)
print("defaultArgs(x,): ", end = ' ')
print("keyword args => defaultArgs(x,): ", end = ' ')
defaultArg(a = 6)


