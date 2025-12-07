# Design a stack class that supports the push, pop, top, and getMin operations.
#
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
#
# Each function should run in O(1)O(1) time.


def __init__(self):
    self.stack = []
    self.min_stack = []


def push(self, val: int) -> None:
    self.stack.append(val)
    if not self.min_stack or val <= self.min_stack[-1]:
        self.min_stack.append(val)


def pop(self) -> None:
    val = self.stack.pop()
    if val == self.min_stack[-1]:
        self.min_stack.pop()


def top(self) -> int:
    return self.stack[-1]


def getMin(self) -> int:
    return self.min_stack[-1]


# o(1) for time
# o(n) for space
# input = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
# output = [null,null,null,null,0,null,2,1]
