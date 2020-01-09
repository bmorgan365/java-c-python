#!/usr/bin/python3
import timeit

fibval = int(input("Enter a value for the fib. seq."))
memo_list = [None] * (fibval + 1)

# fib_test = """
def fib_memo(x):
    if(x < 2): 
        memo_list[x] = 0
        return 0
    if(x == 2): 
        memo_list[x] = 1
        return 1
    if(memo_list[x] != None): 
        return memo_list[x]
    ret = fib(x-1) + fib(x-2)
    memo_list[x] = ret
    return ret
# a = fib(30)
# """

fib2_test = """
def fib2_memo(x):
    if(x < 0): return 0
    if(x == 0 or x == 1): return x
    return fib2(x-1) + fib2(x-2)
b = fib2(30)
"""
# fib_time = timeit.timeit(fib_test, number = 100) / 100
# fib2_time = timeit.timeit(fib2_test, number = 100) / 100
# print("Fib: " + str(fib_time) + "\nFib2: " + str(fib2_time))

print("Fib(" + str(fibval) + "): " + str(fib(fibval)))

