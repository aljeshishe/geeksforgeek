class Solution:
    def reverseInGroups(self, arr, N, K):
        for i in range(0, N, K):
            count = min(K, N-i)
            for front in range(0, count // 2):
                back = count - front - 1
                arr[i + front], arr[i + back] = arr[i + back], arr[i + front]
        return arr



assert Solution().reverseInGroups(arr=[1, 2, 3, 4, 5], N=5, K=3) == [3, 2, 1, 5, 4]
assert Solution().reverseInGroups(arr=[5,6,8,9], N=4, K=3) == [8, 6, 5, 9]
a = "01234"
for i in range(len(a) - 1, -1, -1):
    print(a[i])