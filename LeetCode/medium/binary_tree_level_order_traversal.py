'''
    https://leetcode.com/problems/binary-tree-level-order-traversal/

    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

'''
    Accepted
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: [TreeNode]) -> [[int]]:
        if root is None:
            return []

        levels = []

        Q_current_level = []
        Q_second_level = []

        Q_current_level.append(root)

        while len(Q_current_level) != 0:
            temp_level = []

            while len(Q_current_level) != 0:
                parent = Q_current_level.pop(0)

                temp_level.append(parent.val)

                # put the children in the queue and mark them as visited
                left_child = parent.left
                right_child = parent.right

                if left_child is not None:
                    Q_second_level.append(left_child)

                if right_child is not None:
                    Q_second_level.append(right_child)

            levels.append(temp_level)
            Q_current_level = Q_second_level.copy()
            Q_second_level = []

        return levels


node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

node1 = TreeNode(1)

print(Solution().levelOrder(None))
