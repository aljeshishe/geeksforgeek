# User function Template for python3
class Solution:
    def zigZag(self, arr, n):
        for i in range(len(arr) - 1):
            if i % 2 == 0 and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            elif i % 2 == 1 and arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print(arr)
        return arr


assert Solution().zigZag(arr=[4, 3, 7, 8, 6, 2, 1], n=7) == [3, 7, 4, 8, 2, 6, 1]
assert Solution().zigZag(arr=[1, 4, 3, 2], n=7) == [1, 4, 2, 3]
