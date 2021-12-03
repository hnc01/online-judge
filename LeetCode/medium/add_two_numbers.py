# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
    Accepted Solution but it was a long implementation  which could be reduced to Solution 2
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_head = None
        current_sum_pointer = None

        carry = 0

        while l1 is not None and l2 is not None:
            digit_sum = l1.val + l2.val + carry

            carry = 0

            if digit_sum > 9:
                # we add the last digit of the sum in the sum array
                if sum_head is None:
                    sum_head = ListNode(digit_sum % 10)
                    current_sum_pointer = sum_head
                else:
                    current_sum_pointer.next = ListNode(digit_sum % 10)
                    current_sum_pointer = current_sum_pointer.next

                # the carry becomes the first digit of the digit sum
                carry = int(digit_sum / 10)
            else:
                if sum_head is None:
                    sum_head = ListNode(digit_sum)
                    current_sum_pointer = sum_head
                else:
                    current_sum_pointer.next = ListNode(digit_sum)
                    current_sum_pointer = current_sum_pointer.next

            l1 = l1.next
            l2 = l2.next

        # either both of the lists are empty or only one
        while l1 is not None:
            digit_sum = l1.val + carry

            carry = 0

            if digit_sum > 9:
                # we add the last digit of the sum in the sum array
                if sum_head is None:
                    sum_head = ListNode(digit_sum % 10)
                    current_sum_pointer = sum_head
                else:
                    current_sum_pointer.next = ListNode(digit_sum % 10)
                    current_sum_pointer = current_sum_pointer.next

                # the carry becomes the first digit of the digit sum
                carry = int(digit_sum / 10)
            else:
                if sum_head is None:
                    sum_head = ListNode(digit_sum)
                    current_sum_pointer = sum_head
                else:
                    current_sum_pointer.next = ListNode(digit_sum)
                    current_sum_pointer = current_sum_pointer.next

            l1 = l1.next

        while l2 is not None:
            digit_sum = l2.val + carry

            carry = 0

            if digit_sum > 9:
                # we add the last digit of the sum in the sum array
                if sum_head is None:
                    sum_head = ListNode(digit_sum % 10)
                    current_sum_pointer = sum_head
                else:
                    current_sum_pointer.next = ListNode(digit_sum % 10)
                    current_sum_pointer = current_sum_pointer.next

                # the carry becomes the first digit of the digit sum
                carry = int(digit_sum / 10)
            else:
                if sum_head is None:
                    sum_head = ListNode(digit_sum)
                    current_sum_pointer = sum_head
                else:
                    current_sum_pointer.next = ListNode(digit_sum)
                    current_sum_pointer = current_sum_pointer.next

            l2 = l2.next

        if carry > 0:
            if sum_head is None:
                sum_head = ListNode(carry)
                current_sum_pointer = sum_head
            else:
                current_sum_pointer.next = ListNode(carry)
                current_sum_pointer = current_sum_pointer.next

        # now we are done with adding all the digits of the sum in the array
        return sum_head


'''
    Accepted Solution 2
'''


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # we start off with 0 but we don't care about the initial value of the
        # head because when we return at the end, we return sum_head.next
        # the reason we keep the dummy head is because it removes a lot of None checks in the code
        sum_head = ListNode(0)
        current_sum_pointer = sum_head

        carry = 0

        while l1 is not None or l2 is not None:
            l1_val = 0
            l2_val = 0

            if l1 is not None:
                l1_val = l1.val

            if l2 is not None:
                l2_val = l2.val

            digit_sum = l1_val + l2_val + carry

            carry = 0

            if digit_sum > 9:
                # we add the last digit of the sum in the sum array
                current_sum_pointer.next = ListNode(digit_sum % 10)

                # the carry becomes the first digit of the digit sum
                carry = int(digit_sum / 10)
            else:
                current_sum_pointer.next = ListNode(digit_sum)

            current_sum_pointer = current_sum_pointer.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            current_sum_pointer.next = ListNode(carry)

        # now we are done with adding all the digits of the sum in the array
        return sum_head.next


node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node4.next = node5
node5.next = node6

result = Solution().addTwoNumbers(node1, node4)

while result is not None:
    print(result.val)
    result = result.next
