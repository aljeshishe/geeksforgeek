# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq


def f(points, k):
    heap = []
    for point in points:
        dist = (point[0] **2 + point[1] **2) ** .5
        heapq.heappush(heap, [dist, point[0], point[1]])
    return [heapq.heappop(heap)[1:] for i in range(k)]

def log(v):
    print(v)
    return v

assert log(f([[1,3],[-2,2]], k=1)) == [[-2,2]]
assert log(f([[3,3],[5,-1],[-2,4]], k=2)) == [[3,3],[-2,4]]
