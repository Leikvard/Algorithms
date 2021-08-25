# Uses python3
from sys import stdin
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

#According to the fibonacci spiral square figure, 
#F0^2 + F1^2 + F2^2 + ... + Fn^2 is the total area of the spiral square
#So SumSquare(n) = (F(n - 2) + F(n - 1)) * (F(n - 1) + F(n)), when n = 2
def fib_sum_sqr(n):
    if n <= 2:
        return n

    #get the last digit of the three fibonacci numbers required for getting sum square
    first = period[(n - 2) % period_length]
    second = period[(n - 1) % period_length]
    third = period[(n) % period_length]
    
    return ((first + second ) * (second + third)) % 10

#naive algorithm
def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.readline())
    print(fib_sum_sqr(n))
