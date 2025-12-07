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
    dic = {']': '[', '}': '{', ')': '('}
    for char in s:
        if char in dic.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != dic[char]:
                return False
            stack.pop()

    return len(stack) == 0


s = "[]"
# Output: true
print(valid_p(s))

s2 = "[(])"
# Output: false
