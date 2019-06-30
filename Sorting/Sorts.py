import random
# Implementation of various sorts


# Insertion sort

def insertion_sort(a_list):
    for k in range(1, len(a_list)):
        cur = a_list[k]
        j = k
        while j > 0 and a_list[j-1] > cur:
            a_list[j] = a_list[j - 1]
            j -= 1
            a_list[j] = cur

test_one = []
test_two = []
test_three = []

for i in range(0, 9):
    rand_num = random.randint(0, 15)
    test_one.append(rand_num)
print(test_one)
insertion_sort(test_one)
print("Insertion Sort: ", test_one)
for i in range(0, 9):
    rand_num = random.randint(0, 15)
    test_two.append(rand_num)

print(test_two)
insertion_sort(test_two)
print("Insertion Sort: ", test_two)
for i in range(0, 9):
    rand_num = random.randint(0, 15)
    test_three.append(rand_num)
print(test_three)
insertion_sort(test_three)
print("Insertion Sort: ", test_three)