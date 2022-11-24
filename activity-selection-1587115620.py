def f(a, b):
    pairs = list(zip(a, b))
    pairs.sort(key=lambda x: x[1])
    n = len(a)
    count = 1
    prev = 0
    for i in range(1, n):
        if pairs[i][0] > pairs[prev][1]:
            prev = i
            count += 1
    return count


def v(v):
    print(v)
    return v


assert v(f(a=[1, 3, 2, 5], b=[2, 3, 4, 6])) == 3
assert v(f(a=[2, 1], b=[2, 2])) == 1
assert v(f(a=[1, 3, 2, 5], b=[2, 4, 3, 6])) == 3


