# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        new_head = None
        latest_node = None

        # first we need to set the
        if list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                new_head = list1
                latest_node = list1
                list1 = list1.next
            else:
                new_head = list2
                latest_node = list2
                list2 = list2.next
        elif list1 is not None:
            # list 2 is None
            return list1
        else:
            # list 1 is None and list 2 is not None
            return list2

        # if we reach this stage it means we have 2 lists we need to merge
        # plus it means that new_head is the head of the linked list we need to return
        # latest_node is the latest "sorted" node after merging list1 and list2
        while list1 is not None and list2 is not None:
            # we keep looping while both lists are not empty
            if list1.val <= list2.val:
                latest_node.next = list1
                latest_node = list1
                list1 = list1.next
            else:
                latest_node.next = list2
                latest_node = list2
                list2 = list2.next

        # at this stage we are either done with both lists or there are leftover in one of the lists
        while list1 is not None:
            latest_node.next = list1
            latest_node = list1
            list1 = list1.next

        while list2 is not None:
            latest_node.next = list2
            latest_node = list2
            list2 = list2.next

        return new_head