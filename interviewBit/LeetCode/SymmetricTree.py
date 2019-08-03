

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    return check(root.left, root.right)


def check(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    a = check(left.left, right.right)
    b = check(left.right, right.left)
    return a and b