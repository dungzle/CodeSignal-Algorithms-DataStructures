"""
We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

Given a binary tree t, find the sum of all the numbers encoded in it.

Example
Path 1->0->3 encodes 103
Path 1->0->1 encodes 101
Path 1->4 encodes 14
and their sum is 103 + 101 + 14 = 218.

Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers. It's guaranteed that the sum of encoded integers won't exceed 252.

Guaranteed constraints:
1 ≤ tree size ≤ 2000,
1 ≤ tree depth ≤ 9,
0 ≤ node value ≤ 9.

[output] integer64

The sum of the integers encoded in t, as described above.
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def digitTreeSum(t):
    stack = []
    result = 0
    if not t:
        return 0
    stack.append([t,''])
    while stack:
        v,s = stack.pop()
        if v.left:
            stack.append([v.left,s+str(v.value)])
        if v.right:
            stack.append([v.right,s+str(v.value)])
        print(v.value,' - ',s)
        if (not v.left) and (not v.right):
            s += str(v.value)
            result += int(s)
    return result