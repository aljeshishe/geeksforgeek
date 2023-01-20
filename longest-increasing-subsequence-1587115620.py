# sorted structure if items (value, count)

# scan items backwards. for each item
# for each character
# convert char to num
# multiply on 10^x
# where x changes from n to 0
import sys
from bisect import bisect_right


def f(arr):
    d = [[sys.maxsize, 0]]
    max_ = 0
    for num in arr[::-1]:
        new_item = [num, 0]
        i = bisect_right(d, new_item)
        if i != len(d):
            item = d[i]
            max_count = max([d[j][1] for j in range(i, len(d))])
            new_item[1] = max_count + 1
            max_ = max(max_, new_item[1])
            d.insert(i, new_item)
        else:
            raise ValueError
    return max_


def log(v):
    print(v)
    return v


items = list(map(int, "2 10 5 1 8 6 6 6 5".split()))
assert log(f(items)) == 3
assert log(f([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])) == 6
assert log(f([5, 8, 3, 7, 9, 1])) == 3
