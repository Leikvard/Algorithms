# Uses python3
import sys
import math
#import decimal
#decimal.getcontext().prec = 1000000000000
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

#This function uses the formula that Sum(n) = F(n+2) - 1
def fibonacci_sum_last_digit(n):
    if period[(n + 2) % period_length] == 0:
        return 9
    return period[(n + 2) % period_length] - 1

#overflow problem
def fibo(n):
    phi = (1 + math.sqrt(5)) / 2 
    return round(pow(phi, n) / math.sqrt(5))
#Use decimal avoids overflow but still not enough for n=10^18
def fibo1(n):
    phi = decimal.Decimal((1 + math.sqrt(5)) / 2)
    return round(decimal.Decimal(pow(phi, n)) / decimal.Decimal(math.sqrt(5)))
#This function uses tail recursion, using that Sum(n) = Sum(n - 1) + Sum(n - 2) + 1
# but this function has a maximum recursion depth which is 999
def fibonacci_sum_tail_recr(n, a = 0, b = 1):
    if n == 0:
        return a
    
    elif n == 1:
        return b

    return fibonacci_sum_tail_recr(n - 1, b, (a + b + 1) % 10)
    

#This function is provided by instructors
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_last_digit(n))