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
    def dfs(self, node, leaves):
        if node is None:
            # don't append anything to leaves
            # return False to parent because the node is not a leaf => it's not even a node
            return False
        elif node.left is None and node.right is None:
            # add it to leaves
            leaves.append(node.val)
            # tell its parent that it's a leaf
            return True
        else:
            # the node has children
            is_left_leaf = self.dfs(node.left, leaves)
            is_right_leaf = self.dfs(node.right, leaves)

            if is_left_leaf:
                node.left = None

            if is_right_leaf:
                node.right = None

            # we return False here because this node was not a leaf since it had children
            return False

    def findLeaves(self, root: TreeNode) -> [[int]]:
        levels = []

        while True:
            leaves = []

            # this function should fill leaves with all the leaves in tree rooted at `root`
            is_tree_empty = self.dfs(root, leaves)

            if len(leaves) > 0:
                levels.append(leaves)

            if is_tree_empty:
                break

        return levels


# tree = [1, 2, 3, 4, 5]
tree = [1]

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

print(Solution().findLeaves(root))
