import random


def sort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        sort(arr, l, p)
        sort(arr, p + 1, r)

def partition(arr, l, r):
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

for i in range(100):
    unsorted = actual = [random.randint(0, 100) for _ in range(10)]
    sort(actual, 0, len(actual) - 1)
    assert actual == sorted(unsorted)