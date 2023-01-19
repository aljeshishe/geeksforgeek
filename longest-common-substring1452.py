# iterate over columns
    # iterate over rows
        # if c[col] == c[row]
            # set 1 + mat[-1][-1]
def f(s1, s2):
    l1 = len(s1) + 1
    l2 = len(s2) + 1
    d = [[0]*l1 for _ in range(l2)]
    max_ = 0
    for i1 in range(1, l1):
        for i2 in range(1, l2):
            if s1[i1-1] == s2[i2-1]:
                d[i2][i1] = d[i2-1][i1-1] + 1
                max_ = max(max_, d[i2][i1])
    return max_


def log(v):
    print(v)
    return v

assert log(f("adac", "adadac")) == 4
assert log(f("ABCDGH", "ACDGHR")) == 4
assert log(f("ABC", "ACB")) == 1


