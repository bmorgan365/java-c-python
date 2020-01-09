#!/usr/bin/python3
import timeit

fibval = int(input("Enter a vlue for the fibonacci sequence: "))
memo_list = [None] * (fibval + 1)
memo_list2 = [None] * (fibval + 1)
temp = 0

def fib(x):
    if(x < 0): return 0
    if(x <= 1): return x
    return fib(x-1) + fib(x-2)

def fib2(x):
    if(x < 0): return 0
    if(x == 0 or x == 1): return x
    return fib2(x-1) + fib2(x-2)

def fib_memo(x):
    if(x < 0): return 0
    if(x <= 1): 
        memo_list[x] = x
        return x
    if(memo_list[x] != None): 
        return memo_list[x]
    ret = fib_memo(x-1) + fib_memo(x-2)
    memo_list[x] = ret
    return ret

def fib2_memo(x):
    if(x < 0): 
        return 0
    if(x == 0 or x == 1): 
        memo_list2[x] = x
        return x
    if(memo_list2[x] != None): 
        return memo_list2[x]
    ret = fib2_memo(x-1) + fib2_memo(x-2)
    memo_list2[x] = ret
    return ret

#print("Fib: " + str(fib(fibval)) + "\nFib2: " + str(fib2(fibval)) + "\nFib memo: " + str(fib_memo(fibval)) + "\nFib2 memo: " + str(fib2_memo(fibval)))
"""print("fib:")
for i in range(fibval):
    print(str(fib(i))+" ", end=" ")
print("\nfib_memo:")
for i in range(fibval):
    print(str(fib_memo(i)) + " ", end=" ")
print("\nfib2:")
for i in range(fibval):
    print(str(fib2(i)) + " ", end=" ")

print("\nfib2_memo:")
for i in range(fibval):
    print(str(fib2_memo(i)) + " ", end=" ")
"""
print("fib(" + str(fibval) + "): " + str(fib2_memo(fibval)))

