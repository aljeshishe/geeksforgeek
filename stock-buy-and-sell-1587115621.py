def f(*arr):
    if len(arr) < 2:
        return []
    n = len(arr)
    i = 0
    res = []
    while True:
        while i < n - 1 and arr[i+1] <= arr[i]:
            i += 1

        if i == n - 1:
            break

        buy_i = i
        i += 1

        while i < n and arr[i] >= arr[i-1]:
            i += 1

        res.append((buy_i, i-1))

        if i == n:
            break
    return res

def p(v):
    print(v)
    return v

assert p(f(4,2,2,2,4)) == [(3, 4)]
a = "57 69 12 59 5 9 29 29 99"
a = list(map(int, a.split()))
assert p(f(*a)) == [(0, 1), (2, 3), (4, 8)]
assert p(f(100,180,260,310,40,535,695)) == [(0, 3), (4, 6)]
