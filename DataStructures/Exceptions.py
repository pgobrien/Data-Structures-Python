
class StackError(Exception):
    """Base Class for Stack Exceptions"""
    pass

class EmptyStackException(StackError):
    """Error an empty stack"""
    pass
