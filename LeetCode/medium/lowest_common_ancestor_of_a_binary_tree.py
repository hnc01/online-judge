'''
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

    236. Lowest Common Ancestor of a Binary Tree

    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
    two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root, p, q, found_count, ancestry, parents):
        if root is not None and found_count < 2:
            if root.val == p or root.val == q:
                found_count += 1

            ancestry_copy = ancestry.copy()

            ancestry_copy.append(root)

            if root.right is not None:
                parents[root.right] = ancestry_copy

            if root.left is not None:
                parents[root.left] = ancestry_copy

            self.dfs(root.right, p, q, found_count, ancestry_copy, parents)
            self.dfs(root.left, p, q, found_count, ancestry_copy, parents)

    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None

        # we have 2 cases:
        # Case 1: one is ancestor of the other
        # Case 2: neither one is an ancestor and they have a common ancestor
        parents = {}
        ancestry = []

        self.dfs(root, p, q, 0, ancestry, parents)

        # now parents[p] has full list of ancestry for p
        # now parents[q] has full list of ancestry for q
        if p not in parents:
            # p is the root of the tree
            return p
        else:
            p_ancestry = parents[p]

        if q not in parents:
            # q is the root of the tree
            return q
        else:
            q_ancestry = parents[q]

        if p in q_ancestry:
            # p is an ancestor of q so it's the LCA
            return p
        elif q in p_ancestry:
            # q is an ancestor of p so it's the LCA
            return q
        else:
            # we need to check if any of p's ancestors
            for i in range(len(p_ancestry) - 1, -1, -1):
                p_ancestor_node = p_ancestry[i]

                if p_ancestor_node in q_ancestry:
                    return p_ancestor_node


tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
# tree = [1,2]
root = None

tree_nodes = []

for i in range(0, len(tree)):
    if tree[i] is None:
        tree_nodes.append(None)
    else:
        tree_nodes.append(TreeNode(tree[i]))

for i in range(0, len(tree_nodes)):
    if (i * 2) + 1 < len(tree_nodes):
        left_child = tree_nodes[(i * 2) + 1]
        tree_nodes[i].left = left_child

    if (i * 2) + 2 < len(tree_nodes):
        right_child = tree_nodes[(i * 2) + 2]
        tree_nodes[i].right = right_child

print(Solution().lowestCommonAncestor(tree_nodes[0], tree_nodes[1], tree_nodes[2]).val)
