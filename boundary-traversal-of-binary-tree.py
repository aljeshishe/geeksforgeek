# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

# {
# Driver Code Starts
# Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
# {
#  Driver Code Starts
import sys

import sys

sys.setrecursionlimit(100000)
# Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left if isinstance(left, (Node, type(None))) else Node(left)
        self.right = right if isinstance(right, (Node, type(None))) else Node(right)

    def __str__(self):
        return str(self.data)
    __repr__ = __str__

def f(root):
    res = []
    middle(root, res)
    return left(root) + res + right(root)

def left(root):
    result = []
    while root is not None:
        result.append(root.data)
        root = root.left
    return result[:-1]

def right(root:Node):
    result = []
    while root is not None:
        result.append(root.data)
        root = root.right
    result.reverse()
    return result[1:-1]

def middle(root: Node, res: list[int]) -> None:
    if root:
        if root.left is None and root.right is None:
            res.append(root.data)
        middle(root.left, res)
        middle(root.right, res)

def log(v):
    print(v)
    return v

assert log(f(buildTree("4 10 N 5 5 N 6 7 N 8 8 N 8 11 N 3 4 N 1 3 N 8 6 N 11 11 N 5 8"))) ==  list(map(int, "4 10 5 6 8 11 3 5 8 8 6 11 11".split()))
l = Node(2, left=4, right=Node(5, left=8, right=9))
r = Node(3, left=6, right=7)
r = Node(1, left=l, right=r)
assert log(f(r)) == list(map(int, "1 2 4 8 9 6 7 3".split()))

l = Node(2,
         left=Node(4, left=6, right=5),
         right=Node(9, left=None, right=Node(3, left=7, right=8))
         )
r = Node(1, left=l)
assert log(f(r)) == list(map(int, "1 2 4 6 5 7 8".split()))
