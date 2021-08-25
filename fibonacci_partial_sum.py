# Uses python3
import sys
#Get period of the last digit of fibonacci number
def fibo_last_digit_period():
    previous = 0
    current  = 1
    period = [0]
    flag = not(current == 0 & previous == 1)
    while flag:
        period.append(current)
        previous, current = current, (previous + current) % 10
        flag = not(current == 0 and previous == 1)

    return period
period = fibo_last_digit_period()
period_length = len(period)

#calculate partial sum from period
#Sum(n) = F(n + 2) - 1
#F(m) + F(m+1) + ... + Fn = Sum(n) - Sum(m - 1) = F(n + 2) - F(m + 1)
def partial_sum(m, n):
    to_last_digit = period[(n + 2) % period_length]
    from_last_digit = period[(m + 1) % period_length]
    if to_last_digit - from_last_digit < 0:
        return 10 + to_last_digit - from_last_digit
    return to_last_digit - from_last_digit

#naive algorithm
def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.readline();
    from_, to = map(int, input.split())
    print(partial_sum(from_, to))
