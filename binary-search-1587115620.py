#User function template for Python

class Solution:
    def binarysearch(self, arr, n, k):
        start = 0
        end = len(arr) - 1
        while start <= end:
            pos = (end + start) // 2
            if k > arr[pos]:
                start = pos + 1
            elif k < arr[pos]:
                end = pos - 1
            elif k == arr[pos]:
                return pos
        return -1



assert Solution().binarysearch(arr=(1, 2, 3, 4, 5), n=5, k=4) == 3
assert Solution().binarysearch(arr=(11, 22, 33, 44, 55), n=5, k=445) == -1
