'''
    https://leetcode.com/problems/path-sum-iii/

    437. Path Sum III

    Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

    The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    Accepted: Brute Force using DFS
'''
class Solution:
    def dfs(self, root, sum_so_far, target_sum):
        if root is None:
            # we reached the end of our path and we never managed to return 1 along the way (since we reached here)
            # so the current path must be invalid
            return 0
        else:
            # we add this current node and we reach our sum down this path then we're done with current path
            if sum_so_far + root.val == target_sum:
                # along the current path, we found a sub-path that matches our target, we add it to the current path's
                # total number of results and we continue down the path to see if there are others
                return 1 + self.dfs(root.left, sum_so_far + root.val, target_sum) + self.dfs(root.right, sum_so_far + root.val, target_sum)
            else:
                # adding the current node doesn't lead to sub-path that matches our sum so we continue down the path without
                # adding a 1 to the total number of results down this path
                return self.dfs(root.left, sum_so_far + root.val, target_sum) + self.dfs(root.right, sum_so_far + root.val, target_sum)

    def pathSum(self, root: [TreeNode], targetSum: int) -> int:
        if root is None:
            # if the tree is empty then there are no paths that can give us targetSum
            return 0

        # when we're done with exploring a path starting with parent, now we need to explore paths starting with children
        return self.dfs(root, 0, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)


# tree = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
# targetSum = 8

# tree = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
# targetSum = 22

tree = [10, -7, 8, 3, None, -5, 5, 0, None, None, None, None, None, None, -3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 1]
targetSum = 3

root = None

if len(tree) > 0:
    tree_nodes = []

    for i in range(0, len(tree)):
        if tree[i] is None:
            tree_nodes.append(None)
        else:
            tree_nodes.append(TreeNode(tree[i]))

    for i in range(0, len(tree_nodes)):
        if tree_nodes[i] is not None:
            if (i * 2) + 1 < len(tree_nodes):
                left_child = tree_nodes[(i * 2) + 1]
                tree_nodes[i].left = left_child

            if (i * 2) + 2 < len(tree_nodes):
                right_child = tree_nodes[(i * 2) + 2]
                tree_nodes[i].right = right_child

    root = tree_nodes[0]

print(Solution().pathSum(root, targetSum))
