import random

random.seed(42)
def sort(arr, l, r):
    print(f"sort: {arr=} {l=} {r=}")
    if l < r:
        p = partition(arr, l, r)
        print(f"partitioned: {arr=} {l=} {r=}")

        sort(arr, l, p - 1)
        print(f"partitioned: {arr=} {l=} {p-1=}")

        sort(arr, p + 1, r)
        print(f"partitioned: {arr=} {p+1=} {r=}")

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i

for i in range(100):
    unsorted = actual = [random.randint(0, 100) for _ in range(5)]
    sort(actual, 0, len(actual) - 1)
    assert actual == sorted(unsorted)