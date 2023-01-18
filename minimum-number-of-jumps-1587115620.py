import sys


def func(arr):
    pos = 0
    count = 0
    while True:
        count += 1
        steps = arr[pos]

        max_value = -sys.maxsize
        max_pos = -1
        for i in range(pos + 1, pos + steps + 1):
            if i == len(arr) - 1:
                return count
            if i + arr[i] > max_value:
                max_value = i + arr[i]
                max_pos = i
        if max_pos == -1:
            return -1
        pos = max_pos

def log(value):
    print(value)
    return value

assert log(func([1, 4, 3, 2, 6, 7])) == 2
assert log(func([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])) == 3
assert log(func([0])) == -1
assert log(func([0, 0])) == -1
assert log(func([1, 0, 0, 0])) == -1
assert log(func([1, 1, 1, 1])) == 3

