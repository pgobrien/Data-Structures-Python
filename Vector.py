"""
A Vector class to help reinforce the creation of classes in Python using the Magic Methods
Learned from the book Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser - Data Structures and Algorithms in Python-Wiley (2013)

Proper Usage is as follows:
v = Vector(5)   <0, 0, 0, 0, 0>
v[1] = 25       <0, 25, 0, 0, 0>
v[-1] = 5       <0, 25, 0, 0, 5>
print(v[4])      5
u = v + v       <0, 50, 0, 0, 10>
print(u)        <0, 50, 0, 0, 10>
for e in v:
    print(e)      0
                  50
                  0
                  0
                  10
"""
import random

class Vector:
    """Multi-dimensional Vector"""

    def __init__(self, dim):
        """Creates a Vector with all zeros"""
        self._coords = [0] * dim

    def __len__(self):
        """Return the dimension"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return the jth coordinate"""
        return self._coords[j]

    def __setitem__(self, j, value):
        """Set the jth coordinate of vector to new value"""
        self._coords[j] = value

    def __add__(self, other):
        """Vector addition"""
        if len(self) != len(other):
            raise ValueError("Incorrect Dimensions")

        new_vector = Vector(len(self))
        for j in range(len(self)):
            new_vector[j] = self[j] + other[j]
        return new_vector

    def __eq__(self, other):
        """Return True if vecot has same coordinates as another"""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vectors are different"""
        return not self == other

    def __str__(self):
        """Produce String representation of Vector"""
        return '<' + str(self._coords)[1: -1] + '>'



if __name__ == '__main__':

    u = Vector(4)
    v = Vector(4)
    x = Vector(6)
    y = u

    for i in range(len(u)):
        u[i] = random.randint(0, 30)

    for i in range(len(u)):
        v[i] = random.randint(0, 30)

    for i in range(len(u)):
        x[i] = random.randint(0, 30)

    print(str(u))
    print(str(v))
    print(str(x))
    print(str(y))

    #print(str(x + v))
    print(u == x)  # Throws error
    print(u != x)

    print(u == y)
    print(u != y)




















