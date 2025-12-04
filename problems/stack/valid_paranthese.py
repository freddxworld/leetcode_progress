# so were gonna be using a stack to keep track of LIFO and dic to keep track of
# close to open
#
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
#
# Return true if s is a valid string, and false otherwise.
#
def valid_p(s: str):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            # tells us if stack is empty or if the corresponding value for char
            # does not match the latest push in stack then return false
            if not stack or pairs[char] != stack[-1]:
                return False
            else:
                stack.pop()

    # will pass back true if stack is empty
    return len(stack) == 0


s = "[]"
# Output: true

s2 = "[(])"
# Output: false
print(valid_p(s2))
