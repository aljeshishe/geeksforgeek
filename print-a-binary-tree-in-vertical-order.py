# https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1?page=4&difficulty[]=1&curated[]=1&sortBy=submissions
from collections import deque

from utils import buildTree


def f(root):
    item = (0, 0, root.data)
    items = [item]
    ff(root, item, items)
    items.sort(key=lambda item: item[:2])
    return [item[2] for item in items]


def ff(root, item, items):
    if root:
        if root.left is not None:
            new_item = (item[0] - 1, item[1] + 1, root.left.data)
            items.append(new_item)
            ff(root.left, new_item, items)
        if root.right is not None:
            new_item = (item[0] + 1, item[1] + 1, root.right.data)
            items.append(new_item)
            ff(root.right, new_item, items)

def log(v):
    print(v)
    return v

assert log(f(buildTree("1 2 3 4 5 6 7 N N N N N 8 N 9"))) == list(map(int, "4 2 1 5 6 3 8 7 9".split()))