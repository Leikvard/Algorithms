# Uses python3
import sys
import math
#use sorting method
def get_majority_element(a):
    count = 0
    mid_index = math.floor(n / 2)
    a.sort()
    mid_elem = a[mid_index]
    for i in range(n):
        if a[i] == mid_elem:
            count += 1
    if count > n / 2:
        return 1
    
    return 0



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a))
    #if get_majority_element(a, 0, n) != -1:
    #    print(1)
    #else:
    #    print(0)
