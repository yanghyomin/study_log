# 2026-06-10

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [None]*self.size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, data):
        if self.isFull( ):
            print('포화상태')
            return
        else:
            self.top += 1
            self.arr[self.top] = data

    def pop(self):
        if self.isEmpty( ):
            print('공백상태')
            return
        else:
            popdata = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return popdata