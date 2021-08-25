# Uses python3
import sys
#get gcd by euclidean algorithm
def gcd_euclidean(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == 1 or b == 1:
        return 1
    elif a <= b:
        return gcd_euclidean(a, b % a)
    else:
        return gcd_euclidean(a % b, b)

#get lcm from gcd
def lcm(a, b):
    gcd = gcd_euclidean(a, b)
    return int(a * b / gcd)


#naive algorithm
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

