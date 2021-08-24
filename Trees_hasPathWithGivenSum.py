"""
Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

This is what this tree looks like:

      4
     / \
    1   3
   /   / \
  -2  1   2
    \    / \
     3  -4 -3

Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 5 · 104,
-1000 ≤ node value ≤ 1000.

[input] integer s

An integer.

Guaranteed constraints:
-4000 ≤ s ≤ 4000.

[output] boolean

Return true if there is a path from root to leaf in t such that the sum of node values in it is equal to s, otherwise return false.
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    queue = []
    if not t:
        return False
    queue.append([t,0])
    while queue:
        x,val = queue.pop(0)
        val += x.value
        if x.left:
            queue.append([x.left,val])
        if x.right:
            queue.append([x.right,val])
        if (not x.left) and (not x.right) and (val == s):
            return True
    return False
