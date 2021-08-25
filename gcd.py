# Uses python3
import sys
#Euclidean algorithm
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

#naive algorithm
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
