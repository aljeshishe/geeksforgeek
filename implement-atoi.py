# scan string
    # n = len(s)
    # for each character
        # convert char to num
        # multiply on 10^x
        # where x changes from n to 0
d = {str(i): i for i in range(10)}

def f(s):
    negative_mult = 1
    if s[0] == "-":
        negative_mult = -1
        s = s[1:]

    result = 0
    l = len(s)
    for i in range(l):
        try:
            num = d[s[i]]
            x = l - i - 1
            result += num * (10**x)
        except KeyError:
            return -1
    return result * negative_mult

def log(v):
    print(v)
    return v
assert log(f("1")) == 1
assert log(f("0")) == 0
assert log(f("-0")) == 0
assert log(f("-11")) == -11
assert log(f("123")) == 123
assert log(f("123")) == 123
assert log(f("21a")) == -1


