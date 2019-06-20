

class MyStack(object):
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None


    def __init__(self):
        self.top = None


    def pop(self):

        if self.top is None:
            return 
