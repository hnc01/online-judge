'''
    https://leetcode.com/problems/reverse-nodes-in-k-group/

    25. Reverse Nodes in k-Group

    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

    k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes
    is not a multiple of k then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
    Accepted
'''


class Solution:
    def getListLength(self, head):
        n = 0
        dummy_head = head

        while dummy_head is not None:
            n += 1
            dummy_head = dummy_head.next

        return n

    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:
        if head is None or k == 1:
            # we don't need to reverse anything
            return head

        # we have at least one node in the list
        # n is the total number of nodes in the list
        n = self.getListLength(head)

        if n < k:
            # we don't have enough nodes in the list to reverse
            return head
        else:
            # the head of the resulting list after reversal
            overall_head = None

            # the number of sublists we need to reverse
            target_sublists = n // k
            # the number of sublists we reversed so far: count goes from 1 to target_sublists
            sublists_count = 1

            # now we are sure we have enough nodes in the list to reverse
            # when k = 1 we return above, so if we reach here, we know that k >= 2
            # also, if we reach here we know that n >= k. So, n >= 2
            # we have at least 2 nodes in the list
            prev = head
            current_sublist_old_head = head
            prev_sublist_tail = None  # the tail of the previous sublist
            current = head.next

            while sublists_count <= target_sublists:
                reverse_count = 1

                # we reverse (k-1) times
                while reverse_count < k:
                    current_next = current.next
                    current.next = prev
                    prev = current
                    current = current_next

                    reverse_count += 1

                # the overall head of the list is the head of the first sublist
                # after being reversed => last element in sublist before reverse
                # => prev when current is the head of the next sublist => i.e.
                # after we exit the loop
                if overall_head is None:
                    overall_head = prev

                if prev_sublist_tail is not None:
                    # the tail of the previous sublist should be linked to the new head of the sublist
                    prev_sublist_tail.next = prev

                # the old head of the current sublist is its tail now
                prev_sublist_tail = current_sublist_old_head
                # now we need to assign the next of the original head of the current sublist
                # that we reversed to the current node
                prev = current
                current_sublist_old_head = current

                if current is not None:
                    current = current.next

                sublists_count += 1

            # to make sure we link the tail of the last sublist to the node that's at the beginning
            # of the remainder of the list (no to be reversed)
            if prev_sublist_tail is not None:
                # the tail of the previous sublist should be linked to the new head of the sublist
                prev_sublist_tail.next = prev

            return overall_head


head = [1, 2, 3, 4]
k = 2

list = []

for val in head:
    list.append(ListNode(val))

for i in range(0, len(list) - 1):
    list[i].next = list[i + 1]

if len(list) > 0:
    head = list[0]
else:
    head = None

new_head = Solution().reverseKGroup(head, k)

while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
