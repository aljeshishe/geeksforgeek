# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
# traverse to n1, find node1 logn
    # while traversing, store parent nodes: parents1
# traverse to n2, find node2 logn
    # while traversing, store parent nodes: parents2
# for each in parents1 iterating from back try to find item in parent2 N * 1
# logn + logn + N* 1 = N
# mem: height of tree
class Node:
    def __init__(self, data, right=None, left=None):
        self.left = left
        self.data = data
        self.right = right

    def __repr__(self):
        return str(self.data)
    __str__ = __repr__

def f(root, n1, n2):
    try:
        parents1 = traverse(root, n1)
        parents2 = set(traverse(root, n2))
    except Exception:
        return -1
    for item in parents1[::-1]:
        if item in parents2:
            return item.data

def traverse(root, n):
    items = [root]
    while items:
        top = items.pop()
        if top == n:
            return
        if top.left is not None:
            items.append(top.left)
        if top.right is not None:
            items.append(top.right)
    return -1
def traverse(root, n, parents=None):
    if parents is None:
        parents = []
    if root is None:
        return
    if root.data == n:
        pass
    parents.append(root) # 3 1 0
    traverse(root.left, n)
    traverse(root.right, n)

def traverse(root, n, parents=None):
    if parents is None:
        parents = []

    if root is None:
        return

    parents.append(root) # 3 1 0
    if root.data == n:
        return parents

    res = traverse(root.left, n, parents)
    if res:
        return res

    res = traverse(root.right, n, parents)
    if res:
        return res
    parents.pop()
    return None


def log(v):
    print(v)
    return v


assert log(f(root=Node(1, left=Node(2), right=Node(3)), n1=2, n2=3)) == 1
root = Node(5,
            left=Node(2,
                      left=Node(3),
                      right=Node(4)
                      )
            )
assert log(f(root, n1=2, n2=3)) == 2
