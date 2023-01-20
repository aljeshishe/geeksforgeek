
def f(arr):
    if len(arr) < 2:
        return arr
    arr = sorted(arr, key=lambda item: item[0])
    stack = [arr[0]]
    for i in range(1, len(arr)):
        item = arr[i]
        top_item = stack[-1]
        if item[0] > top_item[1]:
            stack.append(item)
            continue

        stack.pop()
        new_item = [top_item[0], max(item[1], top_item[1])]
        stack.append(new_item)
    return stack

def log(v):
    print(v)
    return v


assert log(f([[1,3],[2,4],[6,8],[9,10]])) == [[1, 4], [6, 8], [9, 10]]

assert log(f([[6, 8], [1, 9], [2, 4], [4, 7]])) == [[1, 9]]
