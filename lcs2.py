#Uses python3

import sys

def lcs2(a, b):
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
