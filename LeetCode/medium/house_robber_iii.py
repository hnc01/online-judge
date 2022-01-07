'''
    https://leetcode.com/problems/house-robber-iii/

    337. House Robber III

    The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

    Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses
    in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

    Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
    Time Limit Exceeded
'''


class Solution:
    def rob_helper(self, root, is_parent_taken):
        # as we're going down the tree, at some point we will reach a leaf and call this function with root = None
        if root is None:
            # we can't rob anything with a None node
            return 0

        # at each step, we check the amount we'll get by considering the current node and the amount we'd get by skipping this node
        # then we take the max between them

        # if the parent is taken then we can't take the value of the current node as part of the amount
        if is_parent_taken:
            # we need to skip the current root because its parent was used
            return self.rob_helper(root.left, False) + self.rob_helper(root.right, False)
        else:
            # we can skip the current node value OR we can consider the current node value (we can choose which way is best)
            return int(max(self.rob_helper(root.left, False) + self.rob_helper(root.right, False), root.val + self.rob_helper(root.left, True) + self.rob_helper(root.right, True)))

    def rob(self, root: [TreeNode]) -> int:
        return self.rob_helper(root, False)


class Solution2:
    def rob_helper(self, root, memo):
        if root is not None:
            if root.right is None and root.left is None:
                # we are at a leaf node so the most amount we can rob is only the amount at this node
                # memo[root][False] => if the parent was not considered in the amount robbed
                # memo[root][True] => if the parent was considered in the amount robbed
                memo[root] = {}

                memo[root][False] = root.val  # if the parent was not considered then the max we can get from this node is its value
                memo[root][True] = 0  # if the parent was considered then we can't consider the value of this node
            else:
                # we can still explore branches off of this node
                # first we examine the children
                self.rob_helper(root.right, memo)
                self.rob_helper(root.left, memo)

                # now the children's results are in memo

                # the max at this node is between:
                # considering current node: root.val + memo[root.right][True] + memo[root.left][True] (i.e. max of children if parent is taken)
                # not considering current node: memo[root.right][False] + memo[root.left][False]

                memo[root] = {}

                # if the parent of the current node was considered, then the only choice is to consider the max of the children
                memo[root][True] = memo[root.right][False] + memo[root.left][False]

                # if the parent was not considered then we get the max between considering current node and not considering current node
                memo[root][False] = int(max(root.val + memo[root.right][True] + memo[root.left][True], memo[root.right][False] + memo[root.left][False]))

    def rob(self, root: [TreeNode]) -> int:
        if root is None:
            return 0

        memo = {}

        # Base case: when we are at an empty node, the total is 0 no matter if its parent was considered or not
        memo[None] = {}
        memo[None][True] = 0
        memo[None][False] = 0

        self.rob_helper(root, memo)

        return int(max(memo[root][False], memo[root][True]))


# tree = [3, 2, 3, None, 3, None, 1]
# tree = [3, 4, 5, 1, 3, None, 1]
tree = [79, 99, 77, None, None, None, 69, None, 60, 53, None, 73, 11, None, None, None, 62, 27, 62, None, None, 98, 50, None, None, 90, 48, 82, None, None, None, 55, 64, None, None, 73, 56, 6, 47,
        None, 93, None, None, 75, 44, 30, 82, None, None, None, None, None, None, 57, 36, 89, 42, None, None, 76, 10, None, None, None, None, None, 32, 4, 18, None, None, 1, 7, None, None, 42, 64,
        None, None, 39, 76, None, None, 6, None, 66, 8, 96, 91, 38, 38, None, None, None, None, 74, 42, None, None, None, 10, 40, 5, None, None, None, None, 28, 8, 24, 47, None, None, None, 17, 36,
        50, 19, 63, 33, 89, None, None, None, None, None, None, None, None, 94, 72, None, None, 79, 25, None, None, 51, None, 70, 84, 43, None, 64, 35, None, None, None, None, 40, 78, None, None, 35,
        42, 98, 96, None, None, 82, 26, None, None, None, None, 48, 91, None, None, 35, 93, 86, 42, None, None, None, None, 0, 61, None, None, 67, None, 53, 48, None, None, 82, 30, None, 97, None,
        None, None, 1, None, None]

# tree = [1,2]

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

# for i in range(0, len(tree_nodes)):
#     node = tree_nodes[i]
#
#     if node is not None:
#         print(str(i) + " : " + str(node) + " : " + str(node.val))

print(Solution2().rob(root))
