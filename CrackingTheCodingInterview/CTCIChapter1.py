# Questions from Cracking the coding interview Arrays and Strings Chapter


def is_unique(a_string):
    # with a data structure
    counts = {}
    for c in a_string:
        if c in counts:
            return False
        else:
            counts[c] = 1
    return True

def is_unique_v2(a_string):
    # without a data structure
    sorted_string = ''.join(sorted(a_string))
    print(sorted_string[0])
    print(sorted_string[1])
    if sorted_string[0] == sorted_string[1]:
        return False
    else:
        return True

print(is_unique("Hey"))
print(is_unique("Hello"))
print(is_unique("Help"))
print(is_unique("Naah"))
print()
# Not passing due to casing
print(is_unique_v2("Hey"))
print(is_unique_v2("Hello"))
print(is_unique_v2("Help"))
print(is_unique_v2("Naah"))


def check_permutation(string_one, string_two):
    pass


def urlify(a_string):
    pass


def palindrome_permutation(a_string):
    pass


def one_away(string_one, string_two):
    pass


def string_compression(a_string):
    pass


def rotate_matrix(matrix):
    pass

def zero_matrix(matrix):
    pass

def string_rotation(s1, s2):
    pass
