# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import copy
class Solution(object):
    def __init__(self):
        self.stack = []
        self.transcation = []
        self.t_begin = []
        self.v_init = []

    def push(self, value):
        self.stack.append(value)
        if self.t_begin:
            self.transcation.append(['push',value])

    def top(self):
        if len(self.stack) == 0:
            return 0
        else: return self.stack[-1]

    def pop(self):
        if len(self.stack) != 0:
            num = self.stack.pop()
            if self.t_begin:
                self.transcation.append(['pop',num])

    def begin(self):
        self.t_begin.append(True)
        if len(self.t_begin) == 1:
            self.v_init = copy.deepcopy(self.stack)

    def rollback(self):
        if not self.t_begin:
            return False
        elif len(self.t_begin) == 1:
            self.stack = self.v_init
            self.t_begin.pop()
            self.transcation.pop()
            return True
        else:
            self.t_begin.pop()
            if self.transcation[-1][0] == 'pop':
                self.stack.append(self.transcation[-1][1])
            else:
                self.stack.pop()
            self.transcation.pop()
            return True

    def commit(self):
        if self.t_begin:
            self.t_begin.pop()
            self.transcation.pop()
            return True
        else:
           return False


def test():
    # Define your tests here
    sol = Solution()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"
