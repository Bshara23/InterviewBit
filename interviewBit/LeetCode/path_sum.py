#https://leetcode.com/problems/path-sum/submissions/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root: TreeNode, sum: int) -> bool:

    def preorder(root, ss=0):

        if root:

            if not root.left and not root.right:
                if (ss + root.val) == sum:
                    return True
                return False

            # Then recur on left child
            return preorder(root.left, ss + root.val) or preorder(root.right, ss + root.val)

        else:
            return False

    return preorder(root)


