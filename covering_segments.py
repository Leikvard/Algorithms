# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    seg_list = []
    points = []
    for s in segments:
        seg_list.append([s.start, s.end])
    seg_list.sort()
    n = len(seg_list)
    point = -1
    count = 0

    for i in range(n):
        if point < seg_list[i][0]:
            point = seg_list[i][1]
            points.append(point)
            count += 1
        if point > seg_list[i][1]:
            point = seg_list[i][1]
            points[count - 1] = point
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    #print(points)
    print(len(points))
    print(*points)
