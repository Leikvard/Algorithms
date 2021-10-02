# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    n = len(w)
    # create a two dimensional array
    weight = np.zeros((n + 1) * (W + 1), dtype=np.int64).reshape(n + 1, W + 1)
    for k in range(1, W + 1):
        for i in range(1, n + 1):
            weight[i, k] = weight[i - 1, k]
            if w[i - 1] <= k:
                wgt = weight[i - 1, k - w[i - 1]] + w[i - 1]
                if weight[i, k] < wgt:
                    weight[i, k] = wgt
    return weight[n, W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
