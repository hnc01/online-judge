'''
    105. Construct Binary Tree from Preorder and Inorder Traversal

    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


    Given two integer arrays preorder and inorder where preorder is the preorder traversal
    of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''

'''
    Tricks:
    - Realizing that preorder will help us determine the parent of a subtree
    - Realizing that inorder will help us determine the nodes that are in the left subtree and right subtree of a certain node
    - Since in all calls of the helper function we do the `in` operation on subtree, we should make it a set so that the `in` operation
    is O(1) and not O(n); this removes the Time Limit Exceeded error.
'''


def to_string(root):
    to_string_helper(root, "")


def to_string_helper(x, spacer):
    if x.right is not None:
        to_string_helper(x.right, spacer + "\t")

    print(spacer + str(x.val))

    if x.left is not None:
        to_string_helper(x.left, spacer + "\t")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree_helper(self, parent, subtree, preorder, inorder):
        if len(subtree) == 0:
            return None
        elif len(subtree) == 1:
            # we are at a leaf
            return TreeNode(next(iter(subtree)))
        else:
            if parent is None:
                current_root_index = 0
            else:
                # we need to find the parent of the current subtree
                parent_index = preorder.index(parent.val)

                # we need to find the second parent among subtree
                # the second parent is the one right after parent in preorder
                current_root_index = -1

                # choose the parent
                for i in range(parent_index + 1, len(preorder)):
                    if preorder[i] in subtree:
                        current_root_index = i
                        break

            # now we have the parent of the left subtree
            current_root = TreeNode(preorder[current_root_index])

            left_subtree = set()
            right_subtree = set()

            current_root_inorder_index = inorder.index(current_root.val)

            for i in range(0, current_root_inorder_index):
                if inorder[i] in subtree:
                    left_subtree.add(inorder[i])

            for i in range(current_root_inorder_index + 1, len(inorder)):
                if inorder[i] in subtree:
                    right_subtree.add(inorder[i])

            current_root.left = self.build_tree_helper(current_root, left_subtree, preorder, inorder)
            current_root.right = self.build_tree_helper(current_root, right_subtree, preorder, inorder)

            return current_root

    def buildTree(self, preorder: [int], inorder: [int]) -> [TreeNode]:
        # root of the tree is always first element in preorder
        return self.build_tree_helper(None, set(preorder), preorder, inorder)


root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

to_string(root)
