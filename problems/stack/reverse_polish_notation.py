#
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
#
# Return the integer that represents the evaluation of the expression.
#
#     The operands may be integers or the results of other operations.
#     The operators include '+', '-', '*', and '/'.
#     Assume that division between integers always truncates toward zero.
def rpn(arr: list[str]) -> int:
    stack = []
    for char in arr:
        if char in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))

        else:
            stack.append(int(char))
    return stack[-1]

tokens = ["1","2","+","3","*","4","-"]
print(rpn(tokens))
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5
