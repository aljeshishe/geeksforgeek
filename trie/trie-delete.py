# https://practice.geeksforgeeks.org/problems/trie-delete/1?page=1&category[]=Trie&curated[]=1&sortBy=submissions


# User function Template for python3

def idx(c):
    return ord(c) - ord("a")


def child_count(node):
    return sum(1 for child in node.children if child)


class Solution():
    def deleteKey(self, root, key):
        last_node = (root, idx(key[0]))
        node = root
        for c in key:
            i = idx(c)

            if child_count(node) > 1:
                last_node = (node, i)

            node = node.children[i]
            if node is None:
                return

        node.isEndOfWord = False

        if child_count(node):
            return
        i = last_node[1]
        last_node[0].children[i] = None

        return


# last node = root node
# find last node for key. While searching store last node with > 1 nodes and char
# if key not found return 0
# set none on last node at position char
# return 1

# if not found
# {
# Driver Code Starts
# Initial Template for Python 3

class TrieNode:

    def __init__(self, c=""):
        self.c = c
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
    def __repr__(self):
        return self.c

class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()


# use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch) - ord('a')


# Function to insert string into TRIE.
def insert(root, key):
    # if not present, we insert key into trie. If the key is prefix
    # of trie node, we just mark the leaf node.
    for e in key:
        idx = charToIndex(e)

        if not root.children[idx]:
            root.children[idx] = TrieNode(e)

        root = root.children[idx]

    # marking last node as leaf.
    root.isEndOfWord = True


# Function to use TRIE data structure and search the given string.
def search(root, key):
    for e in key:
        idx = charToIndex(e)

        if not root.children[idx]:
            return

        root = root.children[idx]

    # returning true if key is present else false.
    return root.isEndOfWord


def main():
    n = int(input())
    arr = input().strip().split()
    key = input()

    t = Trie()

    for s in arr:
        insert(t.root, s)

    Solution().deleteKey(t.root, key)

    if search(t.root, key):
        print(0)
    else:
        print(1)


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