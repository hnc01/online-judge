class MinStack:
    stack = None

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # check the minimum value stored with the element before it
        # if min_val > val, then the current node's minimum is its own val
        # otherwise its minimum is the minimum of the previous node
        if len(self.stack) > 0:
            # there are elements in the list already
            previous_element, minimum_val = self.stack[len(self.stack) - 1]

            if val < minimum_val:
                # we add to the end of the list with its own value as min
                self.stack.append((val, val))
            else:
                # we add to the end of the list with previous node's min val
                self.stack.append((val, minimum_val))
        else:
            # the stack is empty so we add the val with val as its minimum value
            self.stack.append((val, val))

    def pop(self) -> None:
        # we remove the last element in the list
        self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        # we return the value of the element at the end of the array
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        # the minimum value recorded with the last entry
        return self.stack[len(self.stack) - 1][1]

min_stack = MinStack()
print(min_stack.push(-2))
print(min_stack.push(0))
print(min_stack.push(-3))
print(min_stack.getMin())
print(min_stack.pop())
print(min_stack.top())
print(min_stack.getMin())
