# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    period = [0]

    for _ in range(n - 1):
        period.append(current)
        previous, current = current, (previous + current) % m
        if current == 0 and previous == 1:
            break
    period_length = len(period)

    return (period[n % period_length - 1] + period[n % period_length - 2]) % m

if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
