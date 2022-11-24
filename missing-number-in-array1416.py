class Solution:
    def MissingNumber(self, array, n):
        s = (n + 1) * (n//2)
        if n % 2 == 1:
            s += (n + 1) / 2
        # print(f"{s=}")
        return int(s) - sum(array)

def p(v):
    print(v)
    return v

assert p(Solution().MissingNumber(array=[1, 2, 3, 5], n=5)) == 4
assert p(Solution().MissingNumber(array=[6, 1, 2, 8, 3, 4, 7, 10, 5], n=10)) == 9
