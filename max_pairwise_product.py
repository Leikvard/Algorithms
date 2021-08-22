import numpy
from numpy import random
import time

#algorithm provided by instructors
def max_pairwise_product_first_algo(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

#One alternative algorithm
def max_pairwise_product_second_algo(numbers):
    n = len(numbers)
    max_first = max(numbers[0], numbers[1])
    max_second = min(numbers[0], numbers[1])
    for i in range(2, n):
        if numbers[i] >= max_first:
            max_second = max_first
            max_first = numbers[i]
        elif numbers[i] >= max_second:
            max_second = numbers[i]
    max_product = max_first * max_second

    return max_product

#Another alternative algorithm, this algorithm is fast but changes the input list, so is not optimal
def max_pairwise_product_third_algo(numbers):
    n = len(numbers)
    max_first = max(numbers)
    numbers.remove(max_first)
    if len(numbers) < n - 1:
        max_second = max_first
    else:
        max_second = max(numbers)
    max_product = max_first * max_second
    return max_product

def stress_test1():
    while True:
        numbers = random.randint(100, size=(10))
        if max_pairwise_product_first_algo(numbers) == max_pairwise_product_second_algo(numbers):
            print(numbers)
            print(max_pairwise_product_first_algo(numbers))
        else:
            print(numbers)
            print(max_pairwise_product_first_algo(numbers), max_pairwise_product_second_algo(numbers))
            print("error")
            break

def stress_test2():
    while True:
        numbers = random.randint(100, size=(10))
        numbers = numbers.tolist()
        if max_pairwise_product_first_algo(numbers) == max_pairwise_product_third_algo(numbers):
            print(numbers)
            print(max_pairwise_product_first_algo(numbers))
        else:
            print(numbers)
            print(max_pairwise_product_first_algo(numbers), max_pairwise_product_third_algo(numbers))
            print("error")
            break


def stress_test3():
    while True:
        numbers = random.randint(1000000, size=(1000))
        numbers = numbers.tolist()
        if max_pairwise_product_second_algo(numbers) == max_pairwise_product_third_algo(numbers):
            print(numbers)
            print(max_pairwise_product_third_algo(numbers))
        else:
            print(numbers)
            print(max_pairwise_product_second_algo(numbers), max_pairwise_product_third_algo(numbers))
            print("error")
            break


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_second_algo(input_numbers))

#compare run time between three algorithms
#    numbers = random.randint(100, size=(10000))

#    start_time = time.time()
#    max_product = max_pairwise_product_first_algo(numbers)
#    print("--- Algorithm1 takes %s seconds ---" % (time.time() - start_time))
#    print(max_product)

#    start_time = time.time()
#    max_pairwise_product_second_algo(numbers)
#    print("--- Algorithm2 takes %s seconds ---" % (time.time() - start_time))
#    print(max_pairwise_product_second_algo(numbers))

#    numbers = numbers.tolist()
#    start_time = time.time()
#    max_pairwise_product_third_algo(numbers)
#    print("--- Algorithm3 takes %s seconds ---" % (time.time() - start_time))
#    print(max_pairwise_product_third_algo(numbers))

#run stress_test() to see if algorithms are correct
#    stress_test1()
#    stress_test2()
#    stress_test3()