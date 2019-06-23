from DataStructures.Exceptions import *


class QueueNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue(object):

    def __init__(self):
        self.first = None
        self.last = None


    def add(self, item):
        new_node = QueueNode(item)
        if self.last is not None:
            self.last.next = new_node
        self.last = new_node
        if self.first is None:
            self.first = self.last


    def remove(self):
        if self.first is None:
            raise EmptyStackException
        node_data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return node_data


    def peek(self):
        if self.first is None:
            raise EmptyStackException
        return self.first.data

    def is_empty(self):
        return self.first is None

test_queue = MyQueue()

for i in range(10):
    test_queue.add(i)

for i in range(10):
    data = test_queue.remove()
    print(data)



