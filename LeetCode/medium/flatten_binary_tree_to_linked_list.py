'''
    https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

    114. Flatten Binary Tree to Linked List

    Given the root of a binary tree, flatten the tree into a "linked list":
    - The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    - The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''


def to_string(root):
    to_string_helper(root, "")


def to_string_helper(x, spacer):
    if x.right is not None:
        to_string_helper(x.right, spacer + "\t")

    print(spacer + str(x.val))

    if x.left is not None:
        to_string_helper(x.left, spacer + "\t")


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
    def flatten(self, root: [TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        old_right_subtree = root.right

        root.right = root.left
        self.flatten(root.right)
        self.flatten(old_right_subtree)

        # here we are linking the newly created right_subtree (flattened left_subtree) with the old right_subtree now flattened
        right_subtree = root.right

        if right_subtree is not None:
            while right_subtree.right is not None:
                right_subtree = right_subtree.right

            right_subtree.right = old_right_subtree
        else:
            # in case the left tree was None and we flattened it, there might be
            # nothing to link the old_right_subtree to. So, in this case, we link it
            # back at its parent's right.
            root.right = old_right_subtree

        root.left = None


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node2.left = node3
node2.right = node4
node1.right = node5
node5.right = node6
node5.left = node7

node0 = TreeNode(0)

Solution().flatten(node1)

to_string(node1)
