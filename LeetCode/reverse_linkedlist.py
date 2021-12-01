class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
    Solution 1 [Accepted]: this solution is iterative and they challenge us at the end to do it using recursion.
    Using recursion is basically the same thing as the iterative solution but instead of having a stack element,
    the stack is present implicitly through the recursion.
'''


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []

        while head is not None:
            stack.append(head)

            head = head.next

        new_head = None
        new_list_pointer = None

        while len(stack) > 0:
            current_node = stack.pop()

            if new_head is None:
                new_head = current_node
                new_list_pointer = current_node
            else:
                new_list_pointer.next = current_node
                new_list_pointer = current_node

            if len(stack) == 0:
                # we need to remove the next pointer of the last node
                new_list_pointer.next = None

        return new_head

'''
    Solution2 [Accepted]: done using recursion
'''
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            # we reached the end of our linkedlist
            return head
        else:
            head_of_reversed_list = self.reverseList(head.next)

            # everything after head is now reversed so we need to reverse connections at head
            # making head the next element of its next in original list (i.e. instead node1.next = node2 we now have node2.next = node1)
            head.next.next = head
            # removing the pointer between the current node and the one next to it according to original order
            head.next = None

            return head_of_reversed_list


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

reversed_list = Solution2().reverseList(node1)

while reversed_list is not None:
    print(reversed_list.val)
    reversed_list = reversed_list.next
