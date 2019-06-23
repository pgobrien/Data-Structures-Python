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


class Range:
    """A class to mimic the Range for a better understanding"""
    def __init__(self, start, stop=None, step=1):
        """Initialize an instance"""
        if step == 0:
            raise ValueError('Step cannot be 0')

        if stop is None:
            start, stop = 0, start      # Start will be 0 and stop will be single parameter

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step but not stop to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation of negative"""
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('Index out of range')

        return self._start + k * self._step



