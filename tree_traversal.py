from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left if isinstance(left, (Node, type(None))) else Node(left)
        self.right = right if isinstance(right, (Node, type(None))) else Node(right)


def item_center(root):
    if root:
        item_center(root.left)
        print(root.data, end=" ")
        item_center(root.right)

def item_first(root):
    if root:
        print(root.data, end=" ")
        item_first(root.left)
        item_first(root.right)

def item_last(root):
    if root:
        item_last(root.left)
        item_last(root.right)
        print(root.data, end=" ")

def stack_first(root):
    stack = deque([root])
    while stack:
        top = stack.popleft()
        if top:
            stack.append(top.left)
            stack.append(top.right)
            print(top.data, end=" ")

def stack_last(root):
    stack = deque([root])
    while stack:
        top = stack.pop()
        if top:
            stack.append(top.left)
            stack.append(top.right)
            print(top.data, end=" ")

def stack_(root):
    stack = deque([root])
    while stack:
        top = stack.pop()
        if top:
            stack.append(top.right)
            stack.append(top.left)
            print(top.data, end=" ")

left = Node(2, left=4, right=5)
right = Node(3, left=6, right=7)
node = Node(1, left=left, right=right)

item_center(node)
print()
item_first(node)
print()
item_last(node)
print()

stack_first(node)
print()
stack_last(node)
print()
stack_(node)
print()
