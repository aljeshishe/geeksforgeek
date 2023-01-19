# https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1
def f(arr):
    if len(arr) < 2:
        return arr
    l = len(arr)
    lo = 0
    hi = l - 1
    mx = arr[-1] + 1
    for pos in range(l):
        if pos % 2:
            arr[pos] += (arr[lo] % mx) * mx
            lo += 1
        else:
            arr[pos] += (arr[hi] % mx) * mx
            hi -= 1

    for i in range(l):
        arr[i] //= mx
    return arr


def log(v):
    print(v)
    return v

items = list(map(int, "6 1 5 2 4 3".split()))
assert log(f([1,2,3,4,5,6])) == items
items = list(map(int, "110 10 100 20 90 30 80 40 70 50 60".split()))
assert log(f([10,20,30,40,50,60,70,80,90,100,110])) == items
