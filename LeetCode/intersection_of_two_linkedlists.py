# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        setA = set()

        iteratorA = headA

        # first we go through listA and we put in a set all the nodes in it
        while iteratorA is not None:
            setA.add(iteratorA)

            iteratorA = iteratorA.next

        # then we go over the elements in listB and check if any of the nodes there are in setA
        iteratorB = headB

        while iteratorB is not None:
            if iteratorB in setA:
                return iteratorB

            iteratorB = iteratorB.next

        # if we reached this point then it means we couldn't find any node in listB that's in setA
        # which means we don't have intersections
        return None