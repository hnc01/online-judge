# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isPalindrome(self, level):
        j = len(level) - 1

        for i in range(0, int(len(level) / 2)):
            if level[i] != level[j]:
                return False

            j -= 1

        return True

    # We adopted a variation of a BFS approach
    def isSymmetric(self, root: TreeNode) -> bool:
        # try BFS approach
        Q = []

        Q.append(root)

        while len(Q) != 0:
            current_level = []

            nextQ = []

            while len(Q) != 0:
                current_node = Q.pop(0)

                if current_node is not None:
                    # even if they're None we need to add them because they show us the non-existance of a child
                    nextQ.append(current_node.left)  # level to go through
                    nextQ.append(current_node.right)  # level to go through

                    current_level.append(current_node.val)
                else:
                    # we still need to add this node to current level if it's None because it means we have no children
                    # at this level for the parent root but we might other children from other parent roots and we need
                    # to compare these children with the None children
                    current_level.append(None)

            if not self.isPalindrome(current_level):
                return False

            Q = nextQ.copy()

        return True


one = TreeNode(1)
two_1 = TreeNode(2)
two_2 = TreeNode(2)
three_1 = TreeNode(3)
three_2 = TreeNode(3)
four_1 = TreeNode(4)
four_2 = TreeNode(4)

one.left = two_1
one.right = two_2

two_1.left = three_1
two_1.right = four_1

two_2.left = four_2
two_2.right = three_2

solution = Solution()
print(solution.isSymmetric(one))
