'''
    https://leetcode.com/problems/binary-tree-right-side-view/

    199. Binary Tree Right Side View

    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
    Accepted: Idea is that we traverse the tree in BFS style and at each level we add to our list of nodes the right-most node of the level. 
'''


class Solution:
    def right_side_view_helper(self, root, nodes):
        Q = []
        next_level_nodes = []

        Q.append(root)
        nodes.append(root.val)

        while len(Q) != 0:
            while len(Q) != 0:
                current_node = Q.pop(0)

                if current_node.left is not None:
                    next_level_nodes.append(current_node.left)

                if current_node.right is not None:
                    next_level_nodes.append(current_node.right)

            # take the right-most node in the current level
            if len(next_level_nodes) > 0:
                nodes.append(next_level_nodes[len(next_level_nodes) - 1].val)

            Q = next_level_nodes
            next_level_nodes = []

    def rightSideView(self, root: [TreeNode]) -> [int]:
        if root is None:
            return []

        nodes = []

        self.right_side_view_helper(root, nodes)

        return nodes


#
# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node5 = TreeNode(5)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
#
# node1.left = node2
# node1.right = node3
# node2.right = node5
# node3.right = node4

# node1 = TreeNode(1)
# node3 = TreeNode(3)
#
# node1.left = node3

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node2.left = node4
node1.right = node3

print(Solution().rightSideView(node1))
