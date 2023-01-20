# https://practice.geeksforgeeks.org/problems/largest-bst/1?page=4&difficulty[]=1&curated[]=1&sortBy=submissions
import sys
from collections import namedtuple

from utils import buildTree

Item = namedtuple("Item", ["min_", "max_", "depth"])

IMAX = sys.maxsize
IMIN = -sys.maxsize


def f(root):
    # None node is ok for BST.
    # min_=IMAX, max_=IMIN are special values
    if root is None:
        return Item(min_=IMAX, max_=IMIN, depth=0)
    if root.left is None and root.right is None:
        return Item(min_=root.data, max_=root.data, depth=1)
    left = f(root.left)
    right = f(root.right)
    if left.max_ < root.data < right.min_:
        return Item(min_=min(left.min_, root.data),
                    max_=max(right.max_, root.data),
                    depth=left.depth + right.depth + 1)

    return Item(min_=IMIN, max_=IMAX, depth=max(left.depth, right.depth))


def ff(root):
    return f(root).depth

    #
    # def ff(root):
    #      return f(root)[2]
    #
    # IMIN = -2147483648
    # IMAX = 2147483647
    # def f(root):
    #         if root==None:
    #             return IMAX,IMIN,0
    #         if (root.left==None and root.right==None):
    #             return root.data,root.data,1
    #
    #         left=f(root.left)
    #         right=f(root.right)
    #
    #
    #         ans=[0,0,0]
    #
    #         if left[1]<root.data and right[0]>root.data:
    #             ans[0]=min(left[0],right[0],root.data)
    #             ans[1]=max(right[1],left[1],root.data)
    #             ans[2]=1+left[2]+right[2]
    #             return ans
    #
    #         ans[0]=IMIN
    #         ans[1]=IMAX
    #         ans[2]=max(left[2],right[2])
    #         return ans


def log(v):
    print(v)
    return v


assert log(ff(buildTree("1 3 4 5 N 2 2 3"))) == 2
assert log(ff(buildTree("4 2 5 1"))) == 4
assert log(ff(buildTree("8"))) == 1
assert log(ff(buildTree("1 4 4 6 8 N N"))) == 1
