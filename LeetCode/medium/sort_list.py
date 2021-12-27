'''
    https://leetcode.com/problems/sort-list/

    148. Sort List

    Given the head of a linked list, return the list after sorting it in ascending order.
'''

'''
    Accepted (the leetcode solution applies merge sort on the original list)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: [ListNode]) -> [ListNode]:
        if head is None:
            return None

        arr = []

        head_copy = head

        while head_copy is not None:
            arr.append(head_copy.val)

            head_copy = head_copy.next

        arr.sort()

        arr_nodes = []

        for i in range(0, len(arr)):
            arr_nodes.append(ListNode(arr[i]))

        for i in range(0, len(arr_nodes) - 1):
            arr_nodes[i].next = arr_nodes[i + 1]

        return arr_nodes[0]

node4 = ListNode(4)
node2 = ListNode(2)
node1 = ListNode(1)
node3 = ListNode(3)

node4.next = node2
node2.next = node1
node1.next = node3

sorted_head = Solution().sortList(node4)

while sorted_head is not None:
    print(sorted_head.val)

    sorted_head = sorted_head.next
