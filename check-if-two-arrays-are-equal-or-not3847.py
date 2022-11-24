from collections import defaultdict


class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, A, B, N):
        data = defaultdict(int)
        for i in A:
            data[i] += 1
        for i in B:
            data[i] -= 1
        result = not any(data.values())
        return result

assert Solution().check(A=(1, 2, 5, 4, 0), B=(2, 4, 5, 0, 1), N=5) == True
assert Solution().check(A=(1,2,5), B=(2,4,15), N=3) == False

