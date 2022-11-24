import sys


def f(*arr):
    local_max = 0
    global_max = -sys.maxsize - 1
    for i in arr:
        local_max = max(i, local_max + i)
        global_max = max(local_max, global_max)

    return global_max



def v(v):
    print(v)
    return v

assert v(f(-1,-2,-3,4,-1,2,1,-5,4)) == 6
assert v(f(-1,-2,-3,-4)) == -1
assert v(f(1,2,3,-2,5)) == 9

