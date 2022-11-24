class Solution:
    def subArraySum(self, arr, n, s):
        n = len(arr)
        start = 0
        accum = 0
        for i in range(n):
            accum += arr[i]
            while accum > s and start < i:
                accum -= arr[start]
                start += 1
            if accum == s:
                result = [start+1, i+1]
                return result
        return [-1]
def p(v):
    print(v)
    return v
assert p(Solution().subArraySum(arr=[1, 2, 3, 4,], n=5, s=0)) == [-1]
assert p(Solution().subArraySum(arr=[1, 2, 3, 7, 5], n=5, s=12)) == [2,4]
assert p(Solution().subArraySum(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n=10, s=15)) == [1,5]
a = "135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134"
a = list(map(int, a.split()))
assert p(Solution().subArraySum(arr=a, n=10, s=468)) == [38, 42]
