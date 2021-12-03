# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
    Solution 1 [Accepted]: because they mentioned post as a way to index every node, I used it but it turned out
    I don't really need the index to the node, I just need to know if I've seen it before. This lead
    to Solution 2.
'''
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        # maps every node to its index in the linkedlist
        pos = {}

        # the index starts at 0
        index = 0

        while head is not None:
            # add head to the pos dict
            # if head is already there, it means that we ran into a cycle
            # else we add the head and move on
            if head in pos:
                return True
            else:
                pos[head] = index
                head = head.next
                index += 1

        return False

'''
    Solution 2 [Accepted]: we replaced the dict with a set because we only need to keep track of visited nodes 
'''
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        # keep track of visited nodes
        visited = set()

        while head is not None:
            # add head to the pos dict
            # if head is already there, it means that we ran into a cycle
            # else we add the head and move on
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next

        return False

'''
    Solution 3: There's an existing algorithm to determine if there's a cycle in a linked list called `Floyd's Cycle Finding Algorithm`
    We create 2 pointers that run at different speeds in the linkedlist (one slow and one fast), if at any point the pointers point to the
    same node, it means that there's a cycle because the only way this would happen is if the faster pointer circled back and caught up
    with the slow pointer.
'''
class Solution3:
    def hasCycle(self, head: ListNode) -> bool:
        # the list is empty so trivially there are no cycles
        if head is None:
            return False

        # starts at beginning
        slow = head
        # immediately skips the head
        fast = head.next

        # need to keep running until we find that slow = fast
        while slow != fast:
            # since fast should reach the end of the linkedlist before slow
            # we test whether reached the end of the list through `fast`
            if fast is None or fast.next is None:
                # we need to test for fast.next because in the else we do fast.next.next
                return False
            else:
                slow = slow.next
                fast = fast.next.next

        # we broke out of the loop with no return False, it means that we hit a cycle
        return True

# [3,2,0,-4]
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

solution = Solution3()
print(solution.hasCycle(node1))