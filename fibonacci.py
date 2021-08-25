#tail recursion
def fib(n, a = 0, b = 1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib(n-1, b, a + b)
# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    
    previous = 0
    current = 1

    for i in range(n - 1):
        previous, current = current, previous + current

    return current

n = int(input())
print(fib(n))
