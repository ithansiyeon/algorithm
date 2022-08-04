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
        if self.t_begin and self.t_begin[-1]:
            self.transcation.append(['push',value])
            self.t_begin[-1] = False

    def top(self):
        if len(self.stack) == 0:
            return 0
        else: return self.stack[-1]

    def pop(self):
        if len(self.stack) != 0:
            num = self.stack.pop()
            if self.t_begin and self.t_begin[-1]:
                self.transcation.append(['pop',num])
                self.t_begin[-1] = False

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
    sol = Solution()
    sol.push(4)
    sol.begin()  # start transaction 1
    sol.push(7)  # stack: [4,7]
    sol.begin()  # start transaction 2
    sol.push(2)  # stack: [4,7,2]
    assert sol.rollback() == True  # rollback transaction 2
    assert sol.top() == 7  # stack: [4,7]
    sol.begin()  # start transaction 3
    sol.push(10)  # stack: [4,7,10]
    assert sol.commit() == True  # transaction 3 is committed
    assert sol.top() == 10
    assert sol.rollback() == True  # rollback transaction 1
    assert sol.top() == 4  # stack: [4]
    assert sol.commit() == False  # there is no open

test()

