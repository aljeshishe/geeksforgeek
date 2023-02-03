# https://practice.geeksforgeeks.org/problems/trie-insert-and-search0651/1?page=1&category[]=Trie&curated[]=1&sortBy=submissions
# User function Template for python3

"""
class TrieNode:

    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
"""


# Function to insert string into TRIE.

def insert(root, key):
    node = root
    for c in key:
        idx = ord(c) - ord("a")
        node.children[idx] = node.children[idx] or TrieNode()
        node = node.children[idx]
    node.isEndOfWord = True

    # code here


# Function to use TRIE data structure and search the given string.
def search(root, key):
    node = root
    for c in key:
        idx = ord(c) - ord("a")
        node = node.children[idx]
        if node is None:
            return 0
    return int(node.isEndOfWord)

    # code here


# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class TrieNode:

    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()


# use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch) - ord('a')


def main():
    n = int(input())
    arr = input().strip().split()
    strs = input()

    t = Trie()

    for s in arr:
        insert(t.root, s)

    if search(t.root, strs):
        print(1)
    else:
        print(0)


import io
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
data = """8
the a there answer any by bye their
the
"""
assert test(data, "1")