




def f(arr1, arr2):
    pos1 = pos2 =0
    res = []

    while len(res) < len(arr1) + 1:
        if pos1 >= len(arr1):
            res.append(arr2[pos2])
            pos2 += 1
            continue
        if pos2 >= len(arr2):
            res.append(arr1[pos1])
            pos1 += 1
            continue

        if arr1[pos1] > arr2[pos2]:
            res.append(arr2[pos2])
            pos2 += 1
        else:
            res.append(arr1[pos1])
            pos1 += 1
    return sum(res[-2:])

def log(v):
    print(v)
    return v


assert log(f([2], [2])) == 4
assert log(f([1, 2, 4, 6, 10], [4, 5, 6, 9, 12])) == 11
assert log(f([1, 12, 15, 26, 38], [2, 13, 17, 30, 45])) == 32
