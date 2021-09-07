# python3
import sys


def compute_min_refills(distance, tank, stops):
    refuel = 0
    n = len(stops)
    stops.append(distance)
    for i in range(n):
        if stops[i] > m or stops[i+1] - stops[i] > m:
            return -1
        if stops[i] == m:
            refuel += 1
            stops = [stop - stops[i] for stop in stops]
        if stops[i] < m:
            if stops[i+1] > m:
                refuel += 1
                stops = [stop - stops[i] for stop in stops]
        
    return refuel
                

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #print(d, m, stops)
    print(compute_min_refills(d, m, stops))
