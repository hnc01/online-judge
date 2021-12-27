'''
    https://leetcode.com/problems/linked-list-cycle-ii/

    142. Linked List Cycle II

    Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

    Do not modify the linked list.
'''

'''
    Accepted
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        if head is None:
            return None

        visited = set()

        head_copy = head

        while head_copy is not None:
            if head_copy in visited:
                return head_copy

            visited.add(head_copy)
            head_copy = head_copy.next

        return None


node3 = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
nodem4 = ListNode(-4)

node3.next = node2
node2.next = node0
node0.next = nodem4
nodem4.next = node2

node = Solution().detectCycle(node3)

# node1 = ListNode(1)
# node2 = ListNode(2)
#
# node1.next = node2
# node2.next = node1
#
# node = Solution().detectCycle(node1)

if node:
    print(node.val)
else:
    print("no cycle")
