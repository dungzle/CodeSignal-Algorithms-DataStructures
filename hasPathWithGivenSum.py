#
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
