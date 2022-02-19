'''
    https://leetcode.com/problems/evaluate-reverse-polish-notation/

    150. Evaluate Reverse Polish Notation

    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

    Note that division between two integers should truncate toward zero.

    It is guaranteed that the given RPN expression is always valid. That means the expression
    would always evaluate to a result, and there will not be any division by zero operation.
'''

'''
    Accepted
'''
class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        # def evaluate(first_op, second_op, operand):
        #     if operand == '+':
        #         return first_op + second_op
        #     elif operand == '-':
        #         return first_op - second_op
        #     elif operand == '*':
        #         return first_op * second_op
        #     else:
        #         return int(first_op / second_op)

        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        operands = ['+', '-', '*', '/']

        stack = []

        for token in tokens:
            # note that we don't need operands anymore because we can do
            # if token in operations (as a key)
            if token in operands:
                # pop last 2 from the stack
                # perform the arithmetic
                # push result into the stack
                second_op = stack.pop()
                first_op = stack.pop()

                # the below was evaluate() function in my code but wanted to
                # try the lambda functionality
                operation = operations[token]
                result = operation(first_op, second_op)

                stack.append(int(result))
            else:
                # it's an integer so we push it in the stack
                stack.append(int(token))

        # the final result of the operation will be the last element in the stack
        return stack[0]


# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(Solution().evalRPN(tokens))
