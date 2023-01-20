from collections import deque


def f(arr, c):
    counter = 0
    d = set()
    dll = deque()
    for item in arr:
        try:
            d.remove(item)  # O(1)
            dll.remove(item)  # O(C)
        except KeyError:
            counter += 1

        d.add(item) # O(1)
        dll.append(item) # O(1)
        if len(dll) > c:
            item = dll.popleft() # O(1)
            d.remove(item) # O(1)
    return counter

def log(v):
    print(v)
    return v


assert log(f([5, 0, 1, 3, 2, 4, 1, 0, 5], 4)) == 8
