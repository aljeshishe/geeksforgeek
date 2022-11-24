# User function Template for python3
import random


class Solution:
    def zigZag(self, arr):
        arr = arr.copy()
        count = 1
        while count:
            count = 0
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    count += 1
            print(count, arr)
        return arr

for i in range(1):
    expected = list(range(10))
    shuffle = expected.copy()
    random.shuffle(shuffle)
    actual = Solution().zigZag(arr=shuffle)
    assert actual == expected, f"{actual=}!={expected}"

