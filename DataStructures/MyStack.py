

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):

        if self.top is None:
            raise ValueError("Empty Stack")

        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def peek(self):
        if self.top is None:
            raise ValueError("Empty Stack")
        return self.top.data

    def is_empty(self):
        return self.top is None



