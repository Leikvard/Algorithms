import sys
import math

def binary_search(a, left, right, x):
    if a[0] == x:
        return 0
    while left <= right:
        mid = math.floor((left + right) / 2)
        if x == a[mid] and x != a[mid - 1]:
            return mid
        if x <= a[mid] and x == a[mid - 1]:
            right = mid - 1
        if x > a[mid]:
            left = mid + 1
        if x < a[mid]:
            right = mid - 1
    return - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, 0, n - 1, x), end = ' ')
