



def f(s):
    n = len(s)
    start = 0
    end = 0

    def is_palindrome(l, r):
        nonlocal start, end
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        if end - start < r - l - 1:
            start = l + 1
            end = r

    for i in range(n):
        is_palindrome(l=i, r=i)
        is_palindrome(l=i, r=i+1)
    return s[start: end]

def v(v):
    print(v)
    return v


assert v(f("vnrtysfrzrmzlygfv")) == "rzr"
assert v(f("aaaabbaa")) == "aabbaa"
assert v(f("abc")) == "a"
