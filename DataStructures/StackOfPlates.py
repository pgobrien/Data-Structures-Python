#CTCI Chapter 3 Problem
from DataStructures.MyStack import *

class SetOfStacks:

    def __init__(self, n):
        self.internal_stacks = [MyStack()]
        self.index = 0
        self.threshold = n
        self.size = 0

    def pop(self):
        pass

    def push(self, data):
        pass

        self.internal_stacks[self.index].push(data)

    def current_index(self):
        return self.threshold // self.size


    def pop_at(self, index):
        if index < 0 or index > len(self.internal_stacks)-1:
            raise ValueError("Index out of Range")

        return self.internal_stacks[index].pop()










