
class StackError(Exception):
    """Base Class for Stack Exceptions"""
    pass

class EmptyStackException(StackError):

    """Empty Stack"""
    def __init__(self):
        print("Stack Empty Error")
