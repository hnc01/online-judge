'''
    98. Validate Binary Search Tree
    https://leetcode.com/problems/validate-binary-search-tree/

    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
'''

'''
    Accepted
    
    Trick: We need to keep track of the ancestry to make sure that not only the left and right children of the current
    node relate correctly to it but also related correctly to its ancestry of parents
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBSTHelper(self, root, ancestry):
        if root is None:
            # an empty binary tree is valid
            return True
        elif root.left is None and root.right is None:
            # a tree with one node is valid binary tree
            return True
        else:
            # we have at least one child
            valid_left = True
            valid_right = True

            if root.left is not None:
                valid_left = root.left.val < root.val

                if len(ancestry) > 0:
                    for (node, type) in ancestry:
                        if type == 'right':
                            # we need to be greater than node
                            valid_left = valid_left and node.val < root.left.val
                        else:
                            # we need to be less than node
                            valid_left = valid_left and node.val > root.left.val

                        if not valid_left:
                            break

            if root.right is not None:
                valid_right = root.right.val > root.val

                if len(ancestry) > 0:
                    for (node, type) in ancestry:
                        if type == 'right':
                            # we need to be greater than node
                            valid_right = valid_right and node.val < root.right.val
                        else:
                            # we need to be less than node
                            valid_right = valid_right and node.val > root.right.val

                        if not valid_right:
                            break

            if valid_right and valid_left:
                ancestry_left = ancestry.copy()
                ancestry_right = ancestry.copy()

                ancestry_left.append((root, 'left'))
                ancestry_right.append((root, 'right'))

                return self.isValidBSTHelper(root.left, ancestry_left) and self.isValidBSTHelper(root.right, ancestry_right)
            else:
                return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTHelper(root, [])


'''
node2 = TreeNode(2)
node1 = TreeNode(1)
node3 = TreeNode(3)

node2.left = node1
node2.right = node3

print(Solution().isValidBST(node2))
'''

node1 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node5.left = node1
node5.right = node4
node4.left = node3
node4.right = node6

print(Solution().isValidBST(node5))
