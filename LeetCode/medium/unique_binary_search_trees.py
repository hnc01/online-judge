'''
    https://leetcode.com/problems/unique-binary-search-trees/

    Given an integer n, return the number of structurally unique BST's (binary search trees)
    which has exactly n nodes of unique values from 1 to n.
'''

'''
    Key Ideas:
    - The possible number of subtrees rooted at a node is the cartesian product of the number of BST for its left and right subtrees
    - F(root, nodes) = total number of subtrees rooted at `root` out of the nodes in `nodes`
    - G(nodes) = SUM of F(root, nodes) for every `root` in `nodes`
'''

'''
    The below implementation yields Time Limit Exceeded
'''


class Solution:
    def F(self, root, subtree):
        # F(i,n) number of subtrees rooted at i
        # the F(i,n) is the cartesian product of the number of BST for its left and right subtrees
        left_subtree = [x for x in subtree if x < root]
        right_subtree = [x for x in subtree if x > root]

        return self.G(left_subtree) * self.G(right_subtree)

    def G(self, nodes):
        if len(nodes) == 0 or len(nodes) == 1:
            return 1
        else:
            total_trees = 0

            for node in nodes:
                nodes_copy = nodes.copy()
                nodes_copy.remove(node)

                total_trees += self.F(node, nodes_copy)

            return total_trees

    def numTrees(self, n: int) -> int:
        nodes = list(range(1, n + 1))

        return self.G(nodes)


'''
    Accepted: we just need to memorize the total number of subtrees that could be created from a tree of certain size
    do that we don't have to recompute the entire list of possible subtrees again.
    
    Key idea:
    - For G(n), it does not matter the content of the sequence, but the length of the sequence. This is why we can safely save
    the results of it in a memo without needing to recompute anything because the content of the tree doesn't matter.
'''

'''
    Runtime is: O(N^2) => check leetcode_solutions folder
'''


class Solution2:
    def F(self, root, subtree, memo):
        # F(i,n) number of subtrees rooted at i
        # the F(i,n) is the cartesian product of the number of BST for its left and right subtrees
        left_subtree = [x for x in subtree if x < root]
        right_subtree = [x for x in subtree if x > root]

        return self.G(left_subtree, memo) * self.G(right_subtree, memo)

    def G(self, nodes, memo):
        if len(nodes) == 0 or len(nodes) == 1:
            return 1
        if len(nodes) in memo:
            return memo[len(nodes)]
        else:
            total_trees = 0

            for node in nodes:
                nodes_copy = nodes.copy()
                nodes_copy.remove(node)

                total_trees += self.F(node, nodes_copy, memo)

            memo[len(nodes)] = total_trees

            return total_trees

    def numTrees(self, n: int) -> int:
        nodes = list(range(1, n + 1))
        memo = {}

        return self.G(nodes, memo)


print(Solution2().numTrees(3))
