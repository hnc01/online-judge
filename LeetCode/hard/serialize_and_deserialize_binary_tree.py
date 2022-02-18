'''
    https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

    297. Serialize and Deserialize Binary Tree

    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
    or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm
    should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree
    structure.

    Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format,
    so please be creative and come up with different approaches yourself.
'''

'''
    Accepted
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        # this function returns a string that represents the binary tree in pre-order
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return ''
        else:
            nodes = []

            Q = []
            Q.append(root)

            while len(Q) != 0:
                node = Q.pop(0)

                if node is not None:
                    nodes.append(str(node.val))

                    Q.append(node.left)
                    Q.append(node.right)
                else:
                    nodes.append('None')

            return ','.join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        tree = data.split(',')

        root = TreeNode(int(tree[0]))

        Q = []
        Q.append(root)

        # we start with i = 1 because tree[0] = root
        i = 1

        # we loop over the Q and we use i to iterate over tree
        while len(Q) != 0 and i < len(tree):
            node = Q.pop(0)

            # node's left is at i
            # node's right is at i + 1
            if tree[i] != 'None':
                left = TreeNode(int(tree[i]))
                node.left = left
                Q.append(left)

            if (i + 1) < len(tree) and tree[i + 1] != 'None':
                right = TreeNode(int(tree[i + 1]))
                node.right = right
                Q.append(right)

            i += 2

        return root


# Note: here the 6 and 7 are the children of 4
tree = [1, 2, 3, None, None, 4, 5, 6, 7]

# the below transformation of tree to an actual tree node tree is wrong so don't take it into consideration
# because the below code won't cater for 6 and 7 being the children of 4, they will be ignored because None and
# None that are after 3 can't have children so the pointers i*2+1 and i*2+2 which add up to the indices of 6 and 7
# will be ignored
tree_nodes = []

for i in range(0, len(tree)):
    if tree[i] is None:
        tree_nodes.append(None)
    else:
        tree_nodes.append(TreeNode(tree[i]))

for i in range(0, len(tree_nodes)):
    while i < len(tree_nodes) and tree_nodes[i] is None:
        i += 1

    if i < len(tree_nodes):
        if (i * 2) + 1 < len(tree_nodes):
            left_child = tree_nodes[(i * 2) + 1]
            tree_nodes[i].left = left_child

        if (i * 2) + 2 < len(tree_nodes):
            right_child = tree_nodes[(i * 2) + 2]
            tree_nodes[i].right = right_child
    else:
        break

print(Codec().serialize(tree_nodes[0]))
