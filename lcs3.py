#Uses python3
import sys
import numpy as np

def lcs3(a, b, c):
    m = len(a)
    n = len(b)
    l = len(c)
    #creat a m+1 * n+1 * l+1 three dimentional matrix and set initial value to 0
    matrix = np.zeros((m + 1) * (n + 1) * (l + 1), dtype=np.int64).reshape(m + 1, n + 1, l + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, l + 1):
                ins = max(matrix[i - 1, j, k], matrix[i, j - 1, k], matrix[i, j, k - 1])
                dele = max(matrix[i, j - 1, k - 1], matrix[i - 1, j - 1, k], matrix[i - 1, j, k - 1])
                mis = matrix[i - 1, j - 1, k - 1]
                match = matrix[i - 1, j - 1, k - 1] + 1
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    matrix[i, j, k] = max(ins, dele, match)
                else:
                    matrix[i, j, k] = max(ins, dele, mis)				
    return matrix[m, n, l]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
