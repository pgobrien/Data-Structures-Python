"""
Example of a low level Iterator in Python
"""

class SeqIterator:
    """ Iterator for any sequence type"""


    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """Return the next element, or else raise the StopIteration Exception"""
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        """An iterator must return itself as an iterator"""
        return self