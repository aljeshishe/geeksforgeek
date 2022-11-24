from collections import defaultdict


class Solution:
    def firstElementKTime(self, a, n, k):
        data = defaultdict(int)
        for i in a:
            data[i] += 1
            if data[i] == k:
                return i
        return -1

assert Solution().firstElementKTime(a=(1, 7, 4, 3, 4, 8, 7), n=7, k=2) == 4
assert Solution().firstElementKTime(a=(5, 4, 3, 4), n=4, k=3) == -1
