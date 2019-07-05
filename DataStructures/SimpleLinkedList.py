class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    def delete(self, data):
        if self.head is None:
            raise ValueError("LinkedList is Empty")
        if self.head.get_data() == data:
            self.head = self.head.get_next()
        current = self.head
        while current.get_next() is not None:
            if current.get_next().get_data() == data:
                current.get_next().set_next(None)
                current.set_next(current.get_next().get_next())

            current = current.get_next()
        raise ValueError(str(data) + " not in List")

    def search(self, data):
        current = self.head

        while current is not None:
            if current.get_data() == data:
                return current

            current = current.get_next()

        return None


    def print(self):
        current = self.head
        pretty = []
        while current is not None:
            pretty.append(str(current.get_data()))
            pretty.append(" -> ")
            current = current.get_next()
        pretty.append("None")
        print("".join(pretty))
