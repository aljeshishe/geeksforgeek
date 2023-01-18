# choose random element
# partition array
# if position of pivot == k, return pivot element
# if position of pivot is < k , choose left side (right side otherwise)
# repest from st 1
import heapq


def f(arr, k):
    heap = []
    for i in arr:
        heapq.heappush(heap, i)
    result = None
    for i in range(k):
        result = heapq.heappop(heap)
    return result


def log(value):
    print(value)
    return value

items = list(map(int, "7 10 4 3 20 15".split()))
assert log(f(items, 3)) == 7
