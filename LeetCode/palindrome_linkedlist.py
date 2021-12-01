# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
    Solution 1 [Accepted]: this solution might not be considered with O(1) extra space because the string grows with input
    They suggest that the only solution where we don't use any extra space, is if we work with the given linked list.
    We reverse the linked list in place from the middle onwards and then we compare the elements one by one between first half
    and second half (if the list is odd then we should ignore the middle element because we can't compare it with anything) 
'''
class Solution:
    def isStringPalindrome(self, s):
        j = len(s) - 1

        for i in range(0, int(len(s) / 2)):
            if s[i] != s[j]:
                return False

            j -= 1

        return True

    def isPalindrome(self, head: ListNode) -> bool:
        s = ""

        while head is not None:
            s += str(head.val)

            head = head.next

        return self.isStringPalindrome(s)