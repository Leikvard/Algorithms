# Uses python3
import numpy as np

def edit_distance(s, t):
    m = len(s)
    n = len(t)
    #creat a (m + 1) * (n + 1) two dimentional matrix
    dis = np.zeros((m + 1) * (n + 1), dtype=np.int64).reshape(m + 1, n + 1)
    #set the first column and the first row to i and j
    for i in range(0, m + 1):
        dis[i, 0] = i
    for j in range(0, n + 1):
        dis[0, j] = j
    #calculate edit distance from 0,0 to m,n
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            ins = dis[i - 1, j] + 1
            dele = dis[i, j - 1] + 1
            mis = dis[i - 1, j - 1] + 1
            match = dis[i - 1, j - 1]
            if s[i - 1] == t[j - 1]:
                dis[i, j] = min(ins, dele, match)
            else:
                dis[i, j] = min(ins, dele, mis)
    return dis[m, n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
