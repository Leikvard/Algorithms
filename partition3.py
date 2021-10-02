# Uses python3
import sys
import numpy as np

def partition3(A):
    A.sort()
    s = sum(A) #sum of A
    if s % 3 != 0:
        return 0
    
    ss = int(s / 3) #sum of each subgroup

    #prepare the first bag of souvenir
    Ac = A.copy()
    n = len(Ac)
    #pop_item = [Ac[1]]
    weight = np.zeros((n + 1) * (ss + 1), dtype=np.int64).reshape(n + 1, ss + 1)
    for k in range(1, ss + 1):
        for i in range(1,n + 1):
            weight[i, k] = weight[i - 1, k]
            if Ac[i - 1] <= k:
                wgt = weight[i - 1, k - Ac[i - 1]] + Ac[i - 1]
                if weight[i, k] < wgt:
                    #pop_item.remove(weight[i - 1, k])
                    weight[i, k] = wgt
                    #pop_item.append(Ac[i - 1])
    if weight[n, ss] != ss:
        return 0
    
    #prepare the second bag of souvenir
    #pop_index = list(set(pop_item))
    #for i in pop_item:
    #    Ac.pop[]
    #print(Ac, pop_item)
    #n = len(Ac)
    ss *= 2
    weight = np.zeros((n + 1) * (ss + 1), dtype=np.int64).reshape(n + 1, ss + 1)
    for i in range(1, n + 1):
        for k in range(1,ss + 1):
            weight[i, k] = weight[i - 1, k]
            if Ac[i - 1] <= k:
                wgt = weight[i - 1, k - Ac[i - 1]] + Ac[i - 1]
                if weight[i, k] < wgt:
                    weight[i, k] = wgt
    if weight[n, ss] != ss:
        return 0

    return 1

    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

