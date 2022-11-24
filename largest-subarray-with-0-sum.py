def f(*arr):
    n = len(arr)
    d = {0: -1}
    cur_sum = 0
    max_len = 0
    for i in range(n):
        cur_sum += arr[i]
        if cur_sum in d:
            max_len = max(max_len, i - d[cur_sum])
        else:
            d[cur_sum] = i
    return max_len

def p(v):
    print(v)
    return v
assert p(f(15,-2,2,-8,1,7,10,23)) == 5
assert p(f(-1, 1, -1, 1)) == 4
