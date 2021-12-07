'''
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

'''
    Accepted
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current_head = head

        if head is None:
            return None
        else:
            length = 0

            while current_head is not None:
                length += 1

                current_head = current_head.next

            # now we have the length
            # the index of the node to remove is length - n
            to_delete_index = length - n

            if to_delete_index == 0:
                return head.next
            else:
                index = 0
                current_head = head

                while current_head is not None:
                    if index + 1 == to_delete_index:
                        # remove the next node
                        if current_head.next is not None and current_head.next.next is not None:
                            current_head.next = current_head.next.next
                        else:
                            current_head.next = None

                        return head

                    current_head = current_head.next
                    index += 1

        return head


# test delete first node
# test delete last node
# test delete middle node
# test delete from empty list

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

new_head = Solution().removeNthFromEnd(node1, 5)

while new_head is not None:
    print(new_head.val)

    new_head = new_head.next
