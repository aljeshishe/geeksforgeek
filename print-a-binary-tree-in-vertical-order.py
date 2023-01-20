# https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1?page=4&difficulty[]=1&curated[]=1&sortBy=submissions
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
    item = (0, 0, root.data)
    items = [item]
    ff(root, item, items)
    items.sort(key=lambda item: item[:2])
    return [item[2] for item in items]


def ff(root, item, items):
    if root:
        if root.left is not None:
            new_item = (item[0] - 1, item[1] + 1, root.left.data) # -1 1 2 / -2 2 4
            items.append(new_item)
            ff(root.left, new_item, items)
        if root.right is not None:
            new_item = (item[0] + 1, item[1] + 1, root.right.data) # 1 1 3
            items.append(new_item)
            ff(root.right, new_item, items)

def log(v):
    print(v)
    return v

assert log(f(buildTree("1 2 3 4 5 6 7 N N N N N 8 N 9"))) == list(map(int, "4 2 1 5 6 3 8 7 9".split()))