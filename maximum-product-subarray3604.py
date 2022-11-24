import sys


def f(*arr):
    local_min = 1
    local_max = -1
    global_max = -sys.maxsize - 1
    for i in arr:
        max_ = i * local_max
        min_ = i * local_min
        if min_ > max_:
            min_, max_ = max_, min_

        local_max = max(max_, i)
        local_min = min(min_, i)
        global_max = max(global_max, local_min, local_max)
    return global_max


def v(v):
    print(v)
    return v


assert v(f(6, -3, -10, 0, 2)) == 180
assert v(f(2, 3, 4, 5, -1, 0)) == 120