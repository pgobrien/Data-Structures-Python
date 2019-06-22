from Exceptions import *


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:

    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise EmptyStackException
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item):
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        if self.top is None:
            raise EmptyStackException
        return self.top.data

    def is_empty(self):
        return self.top is None





