#https://practice.geeksforgeeks.org/problems/unique-rows-in-boolean-matrix/1?page=1&category[]=Trie&curated[]=1&sortBy=submissions
# User function Template for python3
import io

L = 2


class Node:
    def __init__(self):
        self.children = [None for _ in range(L)]

    def append(self, value):
        idx = self._to_idx(value)
        node = self.children[idx] or Node()
        self.children[idx] = node
        return node

    @staticmethod
    def _to_idx(value):
        return ord(value) - ord('0')


def uniqueRow(row, col, matrix):
    current = root = Node()
    for pos in range(row * col):
        if pos % col == 0:
            current = root

        current = current.append(matrix[pos])

    res = []
    stack = []
    dfs(root, res, stack)
    return res


def dfs(root, res, stack):
    final = True
    for i in range(1, -1, -1):
        child = root.children[i]
        if child:
            final = False
            stack.append(i)
            dfs(child, res, stack)
            stack.pop()
    if final:
        res.append(stack.copy())


# {
# Driver Code Starts
# Initial Template for Python 3


def main():
    s = input().split()
    row = int(s[0])
    col = int(s[1])
    matrix = input().split()

    a = uniqueRow(row, col, matrix)

    for row in a:
        for value in row:
            print(value, end=" ")
        print("$", end="")
    print()


in_file = None
out_file = None
def input():
    global in_file
    return in_file.readline().strip()

_print = print
def print(*args, **kwargs):
    global out_file
    _print(*args, **kwargs, file=out_file, flush=True)

def test(input_text):
    global in_file
    global out_file
    in_file = io.StringIO(input_text)
    out_file = io.StringIO()
    main()
    result = out_file.getvalue()
    _print(f"Result: {result}")
    return result.strip()

data = """3 4
1 1 0 1 1 0 0 1 1 1 0 1"""
assert test(data) == "1 1 0 1 $1 0 0 1 $"
# } Driver Code Ends