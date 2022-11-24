import sys


def get_maxs(arr):
    maxs = []
    max_ = -sys.maxsize - 1
    for i in arr:
        max_ = max(max_, i)
        maxs.append(max_)
    return maxs

def f(*arr):
    right_maxs = get_maxs(arr)
    left_maxs = get_maxs(arr[::-1])[::-1]
    levels = 0
    for i, v in enumerate(arr):
        level = min(right_maxs[i], left_maxs[i])
        levels += level - v
    return levels

def v(v):
    print(v)
    return v

a = "1 1 5 2 7 6 1 4 2 3"
a = list(map(int, a.split()))
assert v(f(*a)) == 7
assert v(f(3,0,0,2,0,4)) == 10
assert v(f(7,4,0,9)) ==10

