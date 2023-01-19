# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
# iterate over pairs (n, n + 1) (n+1, n+2)...
    # if n knows n+1 and n+1 does not know n
        # store n+1 as candidate
    # if n+1 knows n and n does not know n+1
        # store n as candidate
# check candidates
def f(m):
    if len(m) < 2:
        return -1
    l = len(m)
    prob_celebs = set()
    not_celebs = set()

    for i in range(l-1):
        if m[i][i+1] == 1:
            not_celebs.add(i)
            if i+1 not in not_celebs:
                prob_celebs.add(i+1)
        else:
            not_celebs.add(i+1)
            if i not in not_celebs:
                prob_celebs.add(i)

    for c in prob_celebs:
        s = sum(m[i][c] for i in range(l))
        if s != l - 1:
            continue

        s = sum(m[c][i] for i in range(l))
        if s != 0:
            continue
        return c
    return -1

def log(v):
    print(v)
    return v

m = [[0, 1],
     [1, 0]]

m = [[0, 1, 0],
     [0, 0, 0],
     [0, 1, 0]]
assert log(f(m)) == 1
assert log(f(m)) == -1
