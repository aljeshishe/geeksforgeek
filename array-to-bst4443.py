# https://practice.geeksforgeeks.org/problems/array-to-bst4443/1?page=1&category[]=Data%20Structures&category[]=Mathematical&category[]=Sorting&category[]=STL&category[]=Queue&category[]=Geometric&category[]=priority-queue&curated[]=6&sortBy=submissions
#

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.value)
    __repr__ = __str__
def f(arr):
    root = _f(arr=arr, l=0, r=len(arr)-1)
    return traverse(root)

def traverse(root):
    res = []
    if root:
        res += [root.value]
        res += traverse(root.left)
        res += traverse(root.right)
    return res


def _f(arr, l, r):
    if r-l+1==1:  # if 1 element
        return Node(arr[l])
    if r-l+1 < 1:  # if 0 elements
        return None
    mid = l+(r-l)//2
    left = _f(arr, l, mid - 1)
    right = _f(arr, mid + 1, r)
    node = Node(value=arr[mid], left=left, right=right)
    return node

def log(v):
    print(v)
    return v


assert log(f([1, 2, 3, 4])) == [2, 1, 3, 4] # 4/2=2
assert log(f([1,2,3,4,5,6,7])) == [4,2,1,3,6,5,7] # 7/2=3
