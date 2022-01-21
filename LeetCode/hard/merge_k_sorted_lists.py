'''
    https://leetcode.com/problems/merge-k-sorted-lists/

    23. Merge k Sorted Lists

    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.
'''

# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
    Correct but Time Limit Exceeded
    
    The below solution is O(k x n)
'''


class Solution:
    # note: lists is just a list of nodes where a node is the head of its Linked List
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        result_head = None
        dummy_head = None

        while True:
            min_node = None
            min_index = -1

            for i in range(0, len(lists)):
                list_head = lists[i]

                if list_head is not None:
                    if min_node is None:
                        min_node = list_head
                        min_index = i
                    else:
                        if list_head.val < min_node.val:
                            min_node = list_head
                            min_index = i

            if min_node is None:
                break

            # we move the head to the next node because we already took the current node
            lists[min_index] = lists[min_index].next

            if result_head is None:
                result_head = min_node
                dummy_head = result_head
            else:
                dummy_head.next = min_node
                dummy_head = dummy_head.next

        return result_head


'''
    Accepted: O(n log k) where n (merge complexity) is the number of nodes in a list and k is the number of lists (divide complexity)
'''


class Solution2:
    def mergeKListsHelper(self, collapsed_lists, s, e):
        # we have 2 base cases:
        # base case 1: e - s == 0 => has 1 element
        # base case 2: e - s < 0 => has 0 elements
        if e - s == 0:
            # we have 1 array to handle, in this case we have nothing
            # to do so we just return the array itself
            return collapsed_lists[s]
        elif e - s < 0:
            # we don't have any list to handle so we return an empty list
            return []
        else:
            # we have 2 or more lists to handle

            # first we'll start with implementing the generic case => 3 or more lists
            # -----------------------------------------------------------------------
            #                                DIVIDE
            # -----------------------------------------------------------------------
            middle = (s + e) // 2

            sorted_left = self.mergeKListsHelper(collapsed_lists, s, middle)
            sorted_right = self.mergeKListsHelper(collapsed_lists, middle + 1, e)

            # -----------------------------------------------------------------------
            #                                COMBINE
            # -----------------------------------------------------------------------
            result = []

            # i will help us loop over sorted_left and j over sorted_right
            i = j = 0

            # we combine them into one sorted list
            while i < len(sorted_left) and j < len(sorted_right):
                if sorted_left[i].val <= sorted_right[j].val:
                    if len(result) > 0:
                        result[len(result) - 1].next = sorted_left[i]

                    # we need to take the element from sorted_left
                    result.append(sorted_left[i])

                    i += 1
                else:
                    if len(result) > 0:
                        result[len(result) - 1].next = sorted_right[j]

                    # sorted_left[i] > sorted_right[j]
                    # we need to take the element from sorted_right
                    result.append(sorted_right[j])
                    j += 1

            while i < len(sorted_left):
                if len(result) > 0:
                    result[len(result) - 1].next = sorted_left[i]

                result.append(sorted_left[i])
                i += 1

            while j < len(sorted_right):
                if len(result) > 0:
                    result[len(result) - 1].next = sorted_right[j]

                result.append(sorted_right[j])
                j += 1

            # making sure that the end of the current list always has next = None
            # otherwise we might end up with cycles
            if len(result) > 0:
                result[len(result) - 1].next = None

            return result

    def mergeKLists(self, lists):
        # we will adopt a divide-and-conquer approach
        collapsed_lists = []

        for list in lists:
            collapsed_list = []

            head = list

            while head is not None:
                collapsed_list.append(head)
                head = head.next

            collapsed_lists.append(collapsed_list)

        # now, we have collapsed_lists which contains all the nodes in a list per list and
        # not just the head of the linked list
        # we will used collapsed_lists to adopt a divide and conquer approach
        result = self.mergeKListsHelper(collapsed_lists, 0, len(collapsed_lists) - 1)

        if len(result) > 0:
            return result[0]
        else:
            return None


'''
    Accepted
'''

'''
    We will do same as Solution2 but without creating collapsed_lists.
'''


class Solution3:
    def mergeKListsHelper(self, lists, s, e):
        # we have 2 base cases:
        # base case 1: e - s == 0 => has 1 element
        # base case 2: e - s < 0 => has 0 elements
        if e - s == 0:
            # we have 1 array to handle, in this case we have nothing
            # to do so we just return the array itself
            return lists[s]
        elif e - s < 0:
            # we don't have any list to handle so we return an empty list
            return None
        else:
            # we have 2 or more lists to handle

            # first we'll start with implementing the generic case => 3 or more lists
            # -----------------------------------------------------------------------
            #                                DIVIDE
            # -----------------------------------------------------------------------
            middle = (s + e) // 2

            sorted_left_head = self.mergeKListsHelper(lists, s, middle)
            sorted_right_head = self.mergeKListsHelper(lists, middle + 1, e)

            # -----------------------------------------------------------------------
            #                                COMBINE
            # -----------------------------------------------------------------------
            result = []

            # we combine them into one sorted list
            while sorted_left_head is not None and sorted_right_head is not None:
                if sorted_left_head.val <= sorted_right_head.val:
                    if len(result) > 0:
                        result[len(result) - 1].next = sorted_left_head

                    # we need to take the element from sorted_left
                    result.append(sorted_left_head)
                    sorted_left_head = sorted_left_head.next
                else:
                    if len(result) > 0:
                        result[len(result) - 1].next = sorted_right_head

                    # sorted_left[i] > sorted_right[j]
                    # we need to take the element from sorted_right
                    result.append(sorted_right_head)
                    sorted_right_head = sorted_right_head.next

            while sorted_left_head is not None:
                if len(result) > 0:
                    result[len(result) - 1].next = sorted_left_head

                result.append(sorted_left_head)
                sorted_left_head = sorted_left_head.next

            while sorted_right_head is not None:
                if len(result) > 0:
                    result[len(result) - 1].next = sorted_right_head

                result.append(sorted_right_head)
                sorted_right_head = sorted_right_head.next

            # making sure that the end of the current list always has next = None
            # otherwise we might end up with cycles
            if len(result) > 0:
                result[len(result) - 1].next = None
                return result[0]
            else:
                return None

    def mergeKLists(self, lists):
        # we will adopt a divide-and-conquer approach

        result = self.mergeKListsHelper(lists, 0, len(lists) - 1)

        return result


# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = [[1, 2], [2, 3], [1, 5], [4, 7, 8], [9, 10, 11], [3, 4, 5]]
# lists = [[], [-1, 5, 11], [], [6, 10]]
# lists = []
input = []

for list in lists:
    new_list = []

    for value in list:
        new_list.append(ListNode(value))

    for i in range(0, len(new_list) - 1):
        new_list[i].next = new_list[i + 1]

    if len(new_list) > 0:
        input.append(new_list[0])
    else:
        input.append(None)

result = Solution3().mergeKLists(input)

while result is not None:
    print(result.val)
    print(result.next)
    result = result.next
