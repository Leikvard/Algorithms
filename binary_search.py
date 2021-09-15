# Uses python3
import sys
import math

def binary_search(a, x):
    left, right = 0, len(a) - 1
    mid = math.floor((left + right) / 2)
    while True:
        if x == a[mid]:
            return mid
        if x > a[mid]:
            left = mid + 1
            if mid == math.floor((left + right) / 2):
                return -1
            mid = math.floor((left + right) / 2)
        if x < a[mid]:
            right = mid - 1
            if mid == math.floor((left + right) / 2):
                return -1
            mid = math.floor((left + right) / 2) 

    # write your code here

def compare_array(A, B):
    C = [0] * len(A)
    for i in range(len(B)):
        C[i] = binary_search(A, B[i])
    return C

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
