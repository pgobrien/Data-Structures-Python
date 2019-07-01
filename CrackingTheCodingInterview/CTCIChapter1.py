# Questions from Cracking the coding interview Arrays and Strings Chapter

def is_unique(a_string):
    # with a data structure
    # O(len(a_string)) is O(n)
    counts = {}
    for c in a_string:
        counts[c] = counts.get(c, 0) + 1
    return True

def is_unique_v2(a_string):
    # without a data structure
    sorted_string = "".join(sorted(a_string))
    for i in range(0, len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
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
print()


# Check is string_two is a permutation of string one
# Solves in O(n log n) because of sorting strings
def check_permutation(string_one, string_two):
    if len(string_one) != len(string_two): return False
    return sorted(string_one) == sorted(string_two)

print(check_permutation("hello", "lleho"))
print(check_permutation("pretty", "meh"))
print(check_permutation(" h ello", "lleho  "))
print(check_permutation("hello", "lho"))

def check_permutationV2(string_one, string_two):
    # solves in O(max( len(string_one), len(string_two) ) )
    countsOne = {}

    for c in string_one:
        countsOne[c] = countsOne.get(c, 0) + 1
    for c in string_two:
        countsOne[c] = countsOne.get(c, 0) - 1
    for val in countsOne.values():
        if val != 0:
            return False
    return True


print(check_permutationV2("hello", "lleho"))
print(check_permutationV2("pretty", "meh"))
print(check_permutationV2(" h ello", "lleho  "))
print(check_permutationV2("hello", "lho"))


def urlify(a_string):
    # Replace all spaces with %20
    # easy with built in
    return a_string.replace(' ', '%20')


print(urlify("patrick obrien"))
print(urlify("sir patrick obrien"))
print(urlify("hhmm  not sure  if    more spaces are allowed"))
print()

def urlify_difficult(a_string):
    new_string = []
    for c in a_string.rstrip():
        if c == ' ':
            new_string.append("%20")
        else:
            new_string.append(c)
    return ''.join(new_string)

print(urlify_difficult("patrick obrien"))
print(urlify_difficult("sir patrick obrien"))
print(urlify_difficult("hhmm  not sure  if    more spaces are allowed"))

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
