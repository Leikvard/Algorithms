# Uses python3
import sys
#The relationship between n and k is that k^2 + k <= 2n <= k^2 + 3k
def optimal_summands(n):
    summands = []
    k = 1
    while not (k ** 2 + k <= 2 * n and k ** 2 + 3 * k >= 2 * n ):
        summands.append(k)
        k += 1
    
    summands.append(int(n - (k - 1) * k / 2))

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
