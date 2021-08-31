# Uses python3
import sys
coin_options = [10, 5, 1]
l = len(coin_options)

#assign coins from larger value to lower value
def get_change(m):
    coin_num_list = []
    total_num_coins = 0

    for i in range(l):
        num_coins = m // coin_options[i]
        total_num_coins += num_coins
        m -= num_coins * coin_options[i]
    return total_num_coins

#naive algorithm
def get_change_naive(m):
    total = m
    fives = m // 5
    tens = m // 10
    compare = m

    for num1 in range(total):
        total = m
        total_num_coins = num1
        total -= num1
        for num2 in range(fives):
            total_num_coins += num2
            total -= num2 * 5
            for num3 in range(tens):
                total_num_coins += num3
                total -= num3 * 10
                if total == 0 and total_num_coins <= compare:
                    compare = total_num_coins

    
    return compare

#stress test
#def stress_test():

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
