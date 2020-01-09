#!/usr/bin/python

arr = [4,7,3,0,6,10,29,16,11,1]

def swap(a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

minVal = 0

for i in range(0, len(arr)-1):
    minVal = i
    for j in range(1, len(arr)):
        if(arr[j] <= arr[minVal]):
            minVal = j

    swap(i, minVal)

for i in arr:
    print(i)


