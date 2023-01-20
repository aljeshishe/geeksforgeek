# https://practice.geeksforgeeks.org/problems/check-for-bst/1?page=1&category[]=Data%20Structures&category[]=Mathematical&category[]=Sorting&category[]=STL&category[]=Queue&category[]=Geometric&category[]=priority-queue&curated[]=1&sortBy=submissions


# Tree Node
import sys
from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    def __str__(self):
        return str(self.data)

    __repr__ = __str__


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


def f(root):
    global_max = -sys.maxsize

    def x(root):
        nonlocal global_max
        if root:
            left_max = x(root.left)  # 2
            right_max = x(root.right)  # 1
            global_max = max(global_max, left_max + right_max+ 1)   # 3
            mx = max(left_max, right_max) + 1
            return mx
        return 0

    x(root)
    return global_max



def log(v):
    print(v)
    return v


assert log(f(buildTree("10 20 30 40 60"))) == 4
assert log(f(buildTree("1 2 3"))) == 3
