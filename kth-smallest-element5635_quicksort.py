

def f(arr, k):
    l = 0
    r = len(arr) - 1
    while True:
        p = partition(arr, l, r)
        if r == l == k-1:
            return arr[r]
        if k-1 <= p:
            r = p
        else:
            l = p + 1

def partition(arr, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(arr) - 1

    pivot = arr[l]
    while True:
        while arr[l] < pivot:
            l += 1
        while arr[r] > pivot:
            r -= 1
        if l >= r:
            return r
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1


def log(value):
    print(value)
    return value
# l = [3, 4]
# assert partition(l) == 0
# assert l == [3, 4]
# items = list(map(int, "7 10 4 3 20 15".split()))
# assert log(f(items, 2)) == 4
items = list(map(int, "7 10 4 3 20 15".split()))
assert log(f(items, 3)) == 7
items = list(map(int, "7 10 4 20 15".split()))
assert log(f(items, 4)) == 15
