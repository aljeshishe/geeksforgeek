#https://practice.geeksforgeeks.org/problems/unique-rows-in-boolean-matrix/1?page=1&category[]=Trie&curated[]=1&sortBy=submissions
# User function Template for python3
import io

L = 2


class Node:
    def __init__(self):
        self.children = [None for _ in range(L)]


    @staticmethod
    def _to_idx(value):
        return ord(value) - ord('0')


def uniqueRow(row, col, matrix):
    current = root = Node()
    results = []

    new = False
    line = []

    for pos in range(row * col):
        value = matrix[pos]
        line.append(value)
        idx = Node._to_idx(value)
        if current.children[idx] is None:
            new = True
            current.children[idx] = Node()
        current = current.children[idx]
        if (pos+1) % col == 0:
            current = root
            if new:
                results.append(line)
            line = []
            new = False

    return results


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

def test(input_text, expected):
    global in_file
    global out_file
    in_file = io.StringIO(input_text)
    out_file = io.StringIO()
    main()
    result = out_file.getvalue().strip()
    if result != expected:
        _print(f"{input_text}")
        _print(f"results!= expected\n{result=}\n{expected=}")
    else:
        _print("OK")
    return result

data = """3 4
1 1 0 1 1 0 0 1 1 1 0 1"""
assert test(data, "1 1 0 1 $1 0 0 1 $")
# } Driver Code Ends