'''
    https://leetcode.com/problems/binary-tree-maximum-path-sum/

    124. Binary Tree Maximum Path Sum

    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has
    an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

    The path sum of a path is the sum of the node's values in the path.

    Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''
import random


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
    Note Accepted: Wrong Answer
'''


class Solution:
    def maxPathSum(self, root: [TreeNode]) -> int:
        def maxPathSumHelper(node):
            # if we reach a None node then it can't contribute anything to the
            if node is None:
                return 0
            else:
                # this will help us use the same max_sum variable across all function calls
                nonlocal max_sum

                # we always have 2 choices when we encounter a node
                # we either start a new path comprising of current node AND its left child AND its right child
                # or we continue the path we have when passing through the current node (i.e. parent path). If we're
                # in a parent path, we can't consider both children, we only consider the one with max path.

                # start new path
                new_path_max_sum = node.val + maxPathSumHelper(node.left) + maxPathSumHelper(node.right)

                max_sum = max(max_sum, new_path_max_sum)

                # continue path
                continue_path_max_sum = node.val + max(maxPathSumHelper(node.left), maxPathSumHelper(node.right))

                # we need to return the value of continue_path_max_sum to the parent (i.e. the node that called maxPathSumHelper)
                # because we want to return to it the max path while going through it. If we return new_path_max_sum, then we'd
                # be returning a max sum of a path that doesn't pass through it.
                # the max_sum will check for this value in the parent function call not here.
                return continue_path_max_sum

        if root is None:
            return 0

        # this will help us keep track of maximum sum we've seen so far
        max_sum = float('-inf')

        maxPathSumHelper(root)

        return max_sum


'''
    Accepted
    
    Observation: in a path, we can't have more than one split. In other words, in a valid path, we can have at most one node where
    we consider both its right path and left path. If we have more than one node where we consider both left and right paths then
    the path won't be valid. Furthermore, in a valid path, the node with the split (i.e. considering both its children) is always
    the topmost node (in the path), otherwise the path won't be valid.
    
    So, when we are considering the max paths of children of a node, we can't consider their max paths where we can split at these nodes
    that's why in the recursive call we need to return only the max path where we continue from parent. Otherwise, we won't end up with
    the max sum of a valid path.
    
    At each node, we need to get the max sum of 2 different paths: from parent to node to one of its children (continue path) or from
    node to both of its children (new path). HOWEVER, the children are not REQUIRED to be included in a path because sometimes when the
    children are negative, the max path would be just the current node itself without including its children. This is why when we compute
    the max path for the children, we always saturate them to 0 if their max sum is negative effectively ignoring them. 
'''


class Solution2:
    def maxPathSum(self, root: [TreeNode]) -> int:
        def maxPathSumHelper(node):
            # if we reach a None node then it can't contribute anything to the
            if node is None:
                return 0
            else:
                # this will help us use the same max_sum variable across all function calls
                nonlocal max_sum

                # we always have 2 choices when we encounter a node
                # we either start a new path comprising of current node AND its left child AND its right child
                # or we continue the path we have when passing through the current node (i.e. parent path). If we're
                # in a parent path, we can't consider both children, we only consider the one with max path.

                # by doing max between the actual max sum of a node and 0, we'd be effectively ignoring the children paths
                # when their max sums are negative.
                left_max_sum = max(maxPathSumHelper(node.left), 0)
                right_max_sum = max(maxPathSumHelper(node.right), 0)

                # start new path
                new_path_max_sum = node.val + left_max_sum + right_max_sum

                max_sum = max(max_sum, new_path_max_sum)

                # continue path
                continue_path_max_sum = node.val + max(left_max_sum, right_max_sum)

                # we need to return the value of continue_path_max_sum to the parent (i.e. the node that called maxPathSumHelper)
                # because we want to return to it the max path while going through it. If we return new_path_max_sum, then we'd
                # be returning a max sum of a path that doesn't pass through it.
                # the max_sum will check for this value in the parent function call not here.
                return continue_path_max_sum

        if root is None:
            return 0

        # this will help us keep track of maximum sum we've seen so far
        max_sum = float('-inf')

        maxPathSumHelper(root)

        return max_sum


# tree = [-10, 9, 20, None, None, 15, 7]
# tree = [1, 2, 3]
# tree = [4]

# tree = []
#
# for _ in range(3 * 10**4):
#     tree.append(0)
#
# tree[0] = 1
# tree[1] = 2
# tree[2] = 4

# tree = []
#
# for _ in range(3 * 10**4):
#     tree.append(random.randint(-1000,1000))

# tree = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]

tree = [2, -1]

root = None

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

print(Solution2().maxPathSum(root))
