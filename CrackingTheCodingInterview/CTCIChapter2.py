# Cracking the Coding Interview Chapter 2 Answers
from DataStructures.NodeList import *

def remove_dups():
    head = create_Linked()
    print_list(head)
    exists = set()

    current = head
    exists.add(current.val)

    while current.next is not None:

        if current.next.val not in exists:
            exists.add(current.next.val)
            current = current.next
        else:
            print(current.next.val)
            current.next = current.next.next

    return head

# print_list(remove_dups())
# print()
# print_list(remove_dups())
# print()
# print_list(remove_dups())
# print()
# print_list(remove_dups())
# print()

def return_kth_to_last(head, k):
    print_list(head)
    print("k:" + str(k))
    current = head
    position = 1
    second_run = False

    while True:
        if current is None:
            second_run = True
            current = head

        if position == (k + 1) and second_run:
            return current.val

        if second_run:
            position -= 1
        else:
            position += 1

        current = current.next

# print(return_kth_to_last(create_Linked(), 1))
# print()
# print(return_kth_to_last(create_Linked(), 3))
# print()
# print(return_kth_to_last(create_Linked(), 5))
# print()




#     1 -> 2 -> 3 -> 4 -> 5
#     5 -> 4 -> 3 -> 2 -> 1

def delete_middle_node(head):
    pass



def partition(linked):
    pass

def sum_lists(link_one, link_two):
    pass

def palindrome(linked):
    pass

def intersection(link_one, link_two):
    pass



temp = ListNode(5)
temp.next = ListNode(13)
temp.next.next = ListNode(7)
temp.next.next.next = ListNode(1)
temp.next.next.next.next = ListNode(2)
temp.next.next.next.next.next = temp

def loop_detection(head):
    current = head.next

    while current is not None:

        if current is head:
            return True

        current = current.next

    return False

print(loop_detection(create_Linked()))
print()
print(loop_detection(create_Linked()))
print()
print(loop_detection(temp))


def reverse_linked(head):
    print_list(head)
    current = head
    stack = []

    while current is not None:
        stack.append(current.val)
        current = current.next

    new = ListNode(stack.pop())
    meh = new

    while stack:
        new.next = ListNode(stack.pop())
        new = new.next

    return meh

# print_list(reverse_linked(create_Linked()))
# print()
# print_list(reverse_linked(create_Linked()))
# print()
# print_list(reverse_linked(create_Linked()))
# print()
# print_list(reverse_linked(create_Linked()))
# print()
# print_list(reverse_linked(create_Linked()))
# print()











