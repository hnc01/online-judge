# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0

    def longest_path(self, root):
        if root is None:
            # we reached the end of a path down the tree
            return 0
        else:
            # we need to get the longest path down the left and right children
            # and see which one is longer
            left_path_length = self.longest_path(root.left)
            right_path_length = self.longest_path(root.right)

            # we don't need to add +1 here because we already count it in the return of longest_path
            self.diameter = max(self.diameter, left_path_length + right_path_length)

            # the point of this function is to return the longest path for the root so
            # we return it at the end
            # we add +1 to count the edge between root and its children
            return max(1 + left_path_length, 1 + right_path_length)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.longest_path(root)

        return self.diameter