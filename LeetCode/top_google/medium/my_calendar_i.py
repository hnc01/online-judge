'''
    https://leetcode.com/problems/my-calendar-i/

    729. My Calendar I

    You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

    A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

    The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end),
    the range of real numbers x such that start <= x < end.

    Implement the MyCalendar class:
    - MyCalendar() Initializes the calendar object.
    - boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a
      double booking. Otherwise, return false and do not add the event to the calendar.
'''

'''
    Accepted
'''


class MyCalendar:
    class Node:
        # Function to initialise the node object
        def __init__(self, start, end):
            self.start = start  # Assign data
            self.end = end  # Assign data
            self.next = None  # Initialize next as null

    # Linked List class contains a Node object
    class LinkedList:
        # Function to initialize head
        def __init__(self):
            self.head = None

    def __init__(self):
        self.events = self.LinkedList()

    def book(self, start: int, end: int) -> bool:
        if self.events.head is None:
            # insert the event directly
            self.events.head = self.Node(start, end)

            return True
        else:
            # we need to find the first node with node.start > start
            current_node = self.events.head
            previous_node = None

            while current_node is not None and current_node.start < start:
                previous_node = current_node
                current_node = current_node.next

            # the new event will have to be inserted:
            # - between 2 nodes
            # - at the beginning of list
            # - at the end of list

            if previous_node is None:
                # the new event might be inserted at beginning of list
                # need to compare it with head (current_node)
                if (start <= current_node.start and end > current_node.start):
                    return False
                else:
                    # no conflict with head so place it at the beginning
                    new_event = self.Node(start, end)
                    new_event.next = self.events.head
                    self.events.head = new_event

                    return True
            elif current_node is None:
                # the new event might be inserted at the end of list
                # need to compare it with previous_node
                if (previous_node.start <= start and previous_node.end > start):
                    return False
                else:
                    # no conflict with end so place it at the end of list
                    new_event = self.Node(start, end)

                    previous_node.next = new_event

                    return True
            else:
                # we might need to insert the event in the middle of the list
                # now current_node is at the first node that starts after the new event
                # we need to check for conflict between (start, end) and current_node and previous node
                if (previous_node.start <= start and previous_node.end > start) or (start <= current_node.start and end > current_node.start):
                    # we have conflict with one of the nodes so we can't place the event
                    return False
                else:
                    # we don't have conflict with either nodes
                    # we need to place the event between them
                    new_event = self.Node(start, end)

                    previous_node.next = new_event
                    new_event.next = current_node

                    return True


obj = MyCalendar()

parameters = [[10, 20], [15, 25], [20, 30]]

for parameter in parameters:
    print(obj.book(parameter[0], parameter[1]))
