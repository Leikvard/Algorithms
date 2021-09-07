# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    unit = [v / m for v, m in zip(values, weights)]

    total_value = 0
    weight_left = capacity
    
    while weight_left > 0:
        unit_max = max(unit)
        i_max = unit.index(unit_max)
        weight_max = weights[i_max]
        putin = min(weight_max, weight_left)
        weight_left -= putin
        total_value += unit_max * putin

        unit[i_max] = 0

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    #print(n, capacity, data)
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
