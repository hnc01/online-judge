'''
    https://leetcode.com/problems/generate-parentheses/
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

'''
    Accepted
'''

class Solution:
    def generateParenthesisHelper(self, stack_open, stack_closed, result, solutions):
        if len(stack_open) == 0:
            # we need to empty the stack closed and return the string
            while len(stack_closed) > 0:
                result = result + stack_closed.pop()

            solutions.append(result)
        else:
            if len(stack_open) == len(stack_closed):
                # no open but to pop from stack_open
                result = result + stack_open.pop()

                self.generateParenthesisHelper(stack_open.copy(), stack_closed.copy(), result, solutions)
            else:
                # we can either pop from closed or from open
                stack_open_copy = stack_open.copy()
                stack_closed_copy = stack_closed.copy()

                result_open = result + stack_open_copy.pop()
                result_closed = result + stack_closed_copy.pop()

                # pop from open
                self.generateParenthesisHelper(stack_open_copy, stack_closed.copy(), result_open, solutions)
                # pop from closed
                self.generateParenthesisHelper(stack_open.copy(), stack_closed_copy, result_closed, solutions)

    def generateParenthesis(self, n: int) -> []:
        stack_open = []
        stack_closed = []
        solutions = []

        for i in range(0, n):
            stack_open.append("(")
            stack_closed.append(")")

        self.generateParenthesisHelper(stack_open, stack_closed, "", solutions)

        return solutions

print(Solution().generateParenthesis(8))