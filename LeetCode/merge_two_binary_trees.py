# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None and root2 is None:
            return None
        else:
            sum = 0

            root1_left = None
            root1_right = None

            if root1 is not None:
                root1_left = root1.left
                root1_right = root1.right

                sum += root1.val

            root2_left = None
            root2_right = None

            if root2 is not None:
                sum += root2.val

                root2_left = root2.left
                root2_right = root2.right

            merged_root = TreeNode(sum)

            merged_root.left = self.mergeTrees(root1_left, root2_left)
            merged_root.right = self.mergeTrees(root1_right, root2_right)

            return merged_root
