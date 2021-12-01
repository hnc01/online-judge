# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    Accepted
'''
class Solution:
    def invertTreeHelper(self, root):
        if root is not None:
            # the root of the current subtree stays in place, we just flip its children
            temp = root.left
            root.left = root.right
            root.right = temp

            # then we recursively invert the children of the tree
            self.invertTree(root.left)
            self.invertTree(root.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invertTreeHelper(root)

        return root
