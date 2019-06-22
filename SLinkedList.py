from Exceptions import *


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None


    def add_to_tail(self, data):
        end = LinkedNode(data)
        if self.head is None:
            self.head = end
            return
        this = self.head
        while this.next is not None:
            this = this.next
        this.next = end

    def delete_node(self, data):
        if self.head is None:
            return
        temp_node = self.head
        if temp_node.data == data:
            self.head = self.head.next
            return

        while temp_node is not None:
            if temp_node.next is None:
                print("Item not in List")
                break
            if temp_node.next.data == data:
                temp_node.next = temp_node.next.next
                return

            temp_node = temp_node.next

    def print_list(self):
        temp_node = self.head

        while temp_node is not None:
            print(temp_node.data)

            temp_node = temp_node.next


test_Linked = SlinkedList()
for i in range(10):
    test_Linked.add_to_tail(i)
test_Linked.print_list()

test_Linked.delete_node(4)
test_Linked.delete_node(8)
test_Linked.delete_node(15)

test_Linked.print_list()









