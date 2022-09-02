'''

    https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

    428. Serialize and Deserialize N-ary Tree

    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or
    memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children.
    There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary
    tree can be serialized to a string and this string can be deserialized to the original tree structure.
'''

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if root is None:
            return ''
        else:
            result = '( ' + str(root.val) + ' '

            for child in root.children:
                result += self.serialize(child) + ' '

            result += ')'

            return result

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == '':
            return None

        stack = []

        data = data.split(' ')

        for token in data:
            if token == '(':
                stack.append('(')
            elif token == ')':
                # we need to keep popping until we find a (
                children = []

                while stack[-1] != '(':
                    children.append(stack[-1])
                    stack.pop()

                # now we have the last element in stack is the ( so we need to pop that too
                stack.pop()

                # now check if there's anything left in the stack to assign as parent of these children
                if len(stack) > 0:
                    for child in children:
                        stack[-1].children.append(child)
                else:
                    # it means that children has only one node which is the root so we return that
                    return children[0]
            else:
                # it's a value
                stack.append(Node(int(token), []))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
