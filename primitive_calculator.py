# Uses python3
import sys
import math
#dynamic programming
def optimal_sequence(n):
    seq = []
    #check is a dictionary where the key represents the number to be obtained by primitive calculation
    #where is the value is a list where the first integer represents the previous step to obtain the key and the second integer represents the number of operations required
    check = {1:[1, 0], 2:[1, 1], 3:[1, 1]}
    for x in range(4, n + 1):
        #num1, 2, 3 if the minimum number of operations required to obtain n - 1, n // 2 or n // 3
        num1 = check[x - 1][1]
        if x % 2 == 0:
            num2 = check[x // 2][1]
            if x % 3 == 0:
                num3 = check[x // 3][1]
                if num3 == min(num1, num2, num3):
                    check[x] = [x // 3, num3 + 1]
                elif num2 < num1:
                    check[x] = [x // 2, num2 + 1]
                else:
                    check[x] = [x - 1, num1 + 1]
            elif num2 <= num1:
                check[x] = [x // 2, num2 + 1]
            else:
                check[x] = [x - 1, num1 + 1]
        elif x % 3 == 0:
            num3 = check[x // 3][1]
            if num3 <= num1:
                check[x] = [x // 3, num3 + 1]
            else:
                check[x] = [x - 1, num1 + 1]
        else:
            check[x] = [x - 1, num1 + 1]
    i = n
    while i > 1:
        seq.append(i)
        last = check[i][0]
        i = last
    seq.append(1)
    seq.reverse()
    return seq
#using recursive call, slow run time
def optimal_sequence_rec(n):
    sequence = []
    if n <= 3:
        sequence.append(n)
    while n > 1:
        sequence.append(n)
        num1 = len(optimal_sequence(n - 1))
        num2 = len(optimal_sequence(n // 2))
        num3 = len(optimal_sequence(n // 3))
        if n % 2 == 0:
            if n % 3 == 0:
                if num3 == min(num1, num2, num3):
                    n = n // 3
                elif num2 < num1:
                    n = n // 2
                else:
                    n = n - 1
            elif num2 < num1:
                n = n // 2
            else:
                n = n - 1
        elif n % 3 == 0:
            if num3 < num1:
                n = n // 3
            else:
                n = n - 1
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
