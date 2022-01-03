'''
    https://leetcode.com/problems/kth-smallest-element-in-a-bst/

    230. Kth Smallest Element in a BST

    Given the root of a binary search tree, and an integer k, return the kth smallest value
    (1-indexed) of all the values of the nodes in the tree.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_smallest_helper(self, root, k, stack):
        if root is not None and len(stack) <= k:
            # we need to traverse more from the tree
            self.kth_smallest_helper(root.left, k, stack)

            stack.append(root)

            self.kth_smallest_helper(root.right, k, stack)

    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        stack = []

        self.kth_smallest_helper(root, k, stack)

        return stack[k-1].val

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node3.right = node4
node3.left = node1
node1.right = node2

print(Solution().kthSmallest(node3, 1))