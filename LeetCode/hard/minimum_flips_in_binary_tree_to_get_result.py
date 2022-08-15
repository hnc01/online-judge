# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumFlips(self, root: [TreeNode], result: bool) -> int:
        orOp, andOp, xorOp, notOp = 2, 3, 4, 5

        # node is the current node in the tree where we are now
        # target is the target result we need from the current node
        # memo is our dp structure to save calculated results
        def minimumFlipsHelper(node, target, memo):
            # base case: if we are at a leaf
            if node.right is None and node.left is None:
                # here we immediately return the number of flips for this leaf node
                # if they are not equal, the below will result to True => return 1 flip
                # if they are equal, the below will result to False => return 0 flips
                return int(bool(node.val) != target)
            elif (node, target) in memo:
                return memo[(node, target)]
            else:
                # the node has at least one child
                # it means that the current node is an operation and each operation
                # has different ways of achieving a target
                possibilities = {}
                # if OR and target TRUE then we have 3 possible ways of achieving it
                # (l:T, r:F), (l:F, r:T), (l:T, r:T)
                possibilities[(orOp, 1)] = [(1, 0), (0, 1), (1, 1)]
                # if OR and target FALSE then we have 1 possible way of achieving it
                # (l:F, r:F)
                possibilities[(orOp, 0)] = [(0, 0)]
                # if AND and target TRUE then we have 1 possible way of achieving it
                # (l:T, r:T)
                possibilities[(andOp, 1)] = [(1, 1)]
                # if AND and target FALSE then we have 3 possible ways of achieving it
                # (l:T, r:F), (l:F, r:T), (l:F, r:F)
                possibilities[(andOp, 0)] = [(1, 0), (0, 1), (0, 0)]
                # if XOR and target TRUE then we have 2 possible ways of achieving it
                # (l:T, r:F), (l:F, r:T)
                possibilities[(xorOp, 1)] = [(1, 0), (0, 1)]
                # if XOR and target FALSE then we have 2 possible ways of achieving it
                # (l:T, r:T), (l:F, r:F)
                possibilities[(xorOp, 0)] = [(1, 1), (0, 0)]
                # if NOT and target TRUE then we have 1 possible way of achieving it
                # (l:F, r:None)
                possibilities[(notOp, 1)] = [(0, None)]
                # if NOT and target FALSE then we have 1 possible way of achieving it
                # (l:T, r:None)
                possibilities[(notOp, 0)] = [(1, None)]

                minFlips = float('inf')

                for leftTarget, rightTarget in possibilities[(node.val, target)]:
                    if node.val == notOp:
                        # we need to check which child is set
                        if node.right is not None:
                            minFlips = min(minFlips, minimumFlipsHelper(node.right, leftTarget, memo))
                        else:
                            minFlips = min(minFlips, minimumFlipsHelper(node.left, leftTarget, memo))
                    else:
                        minFlips = min(minFlips, minimumFlipsHelper(node.left, leftTarget, memo) + minimumFlipsHelper(node.right, rightTarget, memo))

                memo[(node, target)] = minFlips

                return minFlips

        # if the root is a leaf then we return the result immediately
        if root.left is None and root.right is None:
            # if they are not equal, the below will result to True => return 1 flip
            # if they are equal, the below will result to False => return 0 flips
            return int(bool(root.val) != result)

        # this will map every node and target into its calculated minimum flips
        memo = {}

        return minimumFlipsHelper(root, result, memo)