def f(arr):
    if len(arr) in (0, 2):
        return -1
    if len(arr) == 1:
        return 1
    left = 0
    right = len(arr) - 1
    s_left = s_right = 0
    while True:
        s_left += arr[left]
        left += 1
        print(left, right, s_left, s_right)
        while s_left > s_right and left < right:
            s_right += arr[right]
            right -= 1
        if right == left:
            if s_right == s_left:
                return left + 1
            else:
                return -1


a = "20 17 42 25 32 32 30 32 37 9 2 33 31 17 14 40 9 12 36 21 8 33 6 6 10 37 12 26 21 3"
a = list(map(int, a.split()))
assert f(a) == 13
assert f((1,3,5,2,2)) == 3
assert f((1,)) == 1
