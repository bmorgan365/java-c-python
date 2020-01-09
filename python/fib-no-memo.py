#!/usr/bin/python3
import timeit
#fib_test = """
def fib(x):
    if(x < 2): return 0;
    if(x == 2): return 1;
    return fib(x-1) + fib(x-2)
#a = fib(30)
#"""

fib2_test = """
def fib2(x):
    if(x < 0): return 0
    if(x == 0 or x == 1): return x
    return fib2(x-1) + fib2(x-2)
b = fib2(30)
"""

fibval = int(input("Enter a value for the fib. seq."))
print("Fib(" + str(fibval) + "): " + str(fib(fibval)))

#fib_time = timeit.timeit(fib_test, number = 100) / 100
#fib2_time = timeit.timeit(fib2_test, number = 100) / 100
#print("Fib: " + str(fib_time) + "\nFib2: " + str(fib2_time))
