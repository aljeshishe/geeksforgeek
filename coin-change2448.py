def f(Sum, coins):
    arr = [0] * (Sum+1)
    arr[0] = 1
    for coin in coins:
        for i in range(coin, Sum+1):
            arr[i] += arr[i-coin]
    return arr[-1]

def v(v):
    print(v)
    return v

assert v(f(4, [1,2,3])) == 4
assert v(f(10, [2,5,3,6])) == 5

a = "5 6 7 9 11 12 13 15"
a = list(map(int, a.split()))
assert v(f(9, a)) == 1
