import random

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_Linked():

    head = ListNode(5)
    current = head

    for i in range(random.randint(3, 10)):
        val = random.randint(2, 30)
        current.next = ListNode(val)
        current = current.next

    return head


def print_list(list_node):

    temp = []

    while list_node is not None:

        temp.append(str(list_node.val))
        list_node = list_node.next

    print(" -> ".join(temp))



if __name__ == '__main__':

    test_one = create_Linked()
    test_two = create_Linked()
    test_three = create_Linked()

    print_list(test_one)
    print_list(test_two)
    print_list(test_three)

