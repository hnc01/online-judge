'''
    https://leetcode.com/problems/copy-list-with-random-pointer/

    138. Copy List with Random Pointer

    A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

    Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of
    its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers
    in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

    For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

    Return the head of the copied linked list.

    The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
        - val: an integer representing Node.val
        - random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

    Your code will only be given the head of the original linked list.
'''

'''
    Accepted
'''


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: '[Node]') -> '[Node]':
        if head is None:
            return None

        # map each node to its index
        old_nodes_to_index = {}
        index_to_new_nodes = {}

        # used to loop over the current list
        copy_head = head
        # head of the new list
        new_head = Node(head.val)
        index_to_new_nodes[0] = new_head
        # used to loop over new list
        copy_new_head = new_head

        index = 0

        # this while loop with map each of the nodes in old list to its index
        # this while loop will also create the new list but only through next pointers
        while copy_head is not None:
            old_nodes_to_index[copy_head] = index

            if index != 0:
                new_node = Node(copy_head.val)
                index_to_new_nodes[index] = new_node

                copy_new_head.next = new_node
                copy_new_head = new_node

            copy_head = copy_head.next
            index += 1

        # get the random mapping
        copy_head = head

        # maps old_nodes_index to index of random
        index_to_random_index = {}

        while copy_head is not None:
            if copy_head.random is not None:
                index_to_random_index[old_nodes_to_index[copy_head]] = old_nodes_to_index[copy_head.random]

            copy_head = copy_head.next

        copy_new_head = new_head

        index = 0

        while copy_new_head is not None:
            if index in index_to_random_index:
                copy_new_head.random = index_to_new_nodes[index_to_random_index[index]]

            index += 1
            copy_new_head = copy_new_head.next

        return new_head


node7 = Node(7)
node13 = Node(13)
node11 = Node(11)
node10 = Node(10)
node1 = Node(1)

node7.next = node13
node13.next = node11
node11.next = node10
node10.next = node1

node13.random = node7
node11.random = node1
node10.random = node11
node1.random = node7

new_head = Solution().copyRandomList(node7)

while new_head is not None:
    print('---')

    print("val: " + str(new_head.val))

    if new_head.next is not None:
        print("next: " + str(new_head.next.val))
    else:
        print("next is null")

    if new_head.random is not None:
        print("random: " + str(new_head.random.val))
    else:
        print("random is null")

    print('---')

    new_head = new_head.next
