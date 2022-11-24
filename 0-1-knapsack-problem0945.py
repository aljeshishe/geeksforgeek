def f(W, wt, val):
    N = len(wt)
    d = [[0] * (W+1) for n in range(N+1)]
    for n in range(1, N+1):
        for w in range(1, W+1):
            input_n = n - 1
            prev_max = d[n - 1][w]
            left = w - wt[input_n]
            if left >= 0:
                d[n][w] = max(d[n-1][left] + val[input_n], prev_max)
            else:
                d[n][w] = prev_max
    return d[N][W]

def v(v):
    print(v)
    return v


assert v(f(W=4, wt=[4,5,1], val=[1,2,3])) == 3
assert v(f(W=3, wt=[4,5,6], val=[1,2,3])) == 0
assert v(f(W=50, wt=[10, 20, 30], val=[60, 100, 120])) == 220

