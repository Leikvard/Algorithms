# Uses python3
import sys
import math

def get_change(m):
    coins = [1, 3, 4]
    min_coins = [math.inf] * (m + 1)
    min_coins[0] = 0        
    for money in range(1, m + 1):
        for coin in coins:
            if money >= coin:
                num = min_coins[money - coin] + 1
            if num < min_coins[money]:
                min_coins[money] = num
    return min_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
