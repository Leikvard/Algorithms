#Uses python3

import sys
#auxillary function
def isGreaterOrEqual(a, b):
    if int(a + b) >= int(b + a):
        return True
    else:
        return False
#main function
def largest_number(a):
    #write your code here
    res = ""
    while a:
        maxDigit = '0'
        for x in a:
            if isGreaterOrEqual(x, maxDigit):
                maxDigit = x
        res += maxDigit
        a.remove(maxDigit)
    return int(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
