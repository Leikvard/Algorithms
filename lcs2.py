#Uses python3
import sys
import numpy as np

#Uses python3
import sys
import numpy as np

def lcs2(a, b):
    m = len(a)
    n = len(b)
    #creat a m+1 * n+1 two dimentional matrix and set initial value to 0
    matrix = np.zeros((m + 1) * (n + 1), dtype=np.int64).reshape(m + 1, n + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            ins = matrix[i - 1, j]
            dele = matrix[i, j - 1]
            mis = matrix[i - 1, j - 1]
            match = matrix[i - 1, j - 1] + 1
            if a[i - 1] == b[j - 1]:
                matrix[i, j] = max(ins, dele, match)
            else:
                matrix[i, j] = max(ins, dele, mis)				
    return matrix[i, j]

def lcs(a, b):
    m = len(a) #record the length of sequence a
    n = len(b) #record the length of sequence b
    l = 0 #set initial length of lcs
    index = 0 #set initial first index of lcs
    for i in range(0, m):
        if l < m - i:
            for j in range(0, n):
                if l < n - j:
                    count = 0
                    if a[i] == b[j]:
                        count += 1
                        ii = i + 1
                        jj = j + 1
                        while ii < m and jj < n and a[ii] == b[jj]:
                                count += 1
                                ii += 1
                                jj += 1
                        if l < count:
                            l = count
                            index = i
    if l == 0:
        return l
    return a[index: index + l]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
