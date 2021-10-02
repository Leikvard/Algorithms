# Uses python3
import numpy as np
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    l = len(dataset)
    n = int((l + 1)/2)
    num = [int(dataset[x]) for x in range(0, l, 2)]
    op = [dataset[x] for x in range(1, l, 2)]

    m = np.zeros(n * n, dtype = np.int64).reshape(n, n)
    M = np.zeros(n * n, dtype = np.int64).reshape(n, n)

    for i in range(n):
        m[i, i] = num[i]
        M[i, i] = num[i]
    
    for s in range(1, n):
        for i in range(n - s):
            j = i + s

            mi = math.inf
            ma = - math.inf
            for k in range(i, j):
                a = evalt(m[i, k], m[k + 1, j], op[k])
                b = evalt(m[i, k], M[k + 1, j], op[k])
                c = evalt(M[i, k], M[k + 1, j], op[k])
                d = evalt(M[i, k], m[k + 1, j], op[k])
                mi = min(mi, a, b, c, d)
                ma = max(ma, a, b, c, d)

            m[i, j], M[i, j] = mi, ma 
    return M[0, n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
