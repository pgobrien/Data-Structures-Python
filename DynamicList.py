import ctypes


class DynamicList(object):
    '''
    Dynamic

    '''

    def __init__(self):
        """

        """
        self.size = 0
        self.capacity = 1
        self.internal_array = self.make_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, k):

        if not 0 <= k < self.size:
            return IndexError("Out of Bounds!")

        return self.internal_array[k]

    def add(self, element):

        if self.size == self.capacity:
            self.expand(2 * self.capacity)

        self.internal_array[self.size] = element
        self.size += 1

    def _expand(self, new_capacity):

        temp_array = self.make_array(new_capacity)

        for i in range(self.size):
            temp_array[i] = temp_array[i]

        self.internal_array = temp_array
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
