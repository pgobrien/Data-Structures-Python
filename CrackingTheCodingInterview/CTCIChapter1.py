# Questions from Cracking the coding interview Arrays and Strings Chapter
import random
def generate_matrix(rows, cols):
    return [[random.randint(0, 5) for x in range(cols)] for y in range(rows)]



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
        if sorted_string[i] == sorted_string[i + 1]:
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
print()

# Determine if a string is the permutation of a palindrome
# To do so if the length of the string is even then the counts of all characters must be even
# if the length of the string is odd then only one character count can be odd
def palindrome_permutation(a_string):
    a_string = a_string.lower().replace(' ', "")
    counts = {}
    odd_count = 0

    for letter in a_string:
        counts[letter] = counts.get(letter, 0) + 1

    if len(a_string) % 2 == 0:
        for val in counts.values():
            print(val)
            if val % 2 != 0:
                return False
        return True
    else:
        for val in counts.values():
            if val % 2 != 0 and odd_count > 1:
                return False
            if val % 2 != 0:
                odd_count += 1
        return True

print(palindrome_permutation("Tact Coa"))
print(palindrome_permutation("leloo"))
print(palindrome_permutation("Talloopci"))
print(palindrome_permutation("ce ar rac"))
print()
#Three types of edits on a string:
# insert a character
# remove a character
# replace a character
def one_away(string_one, string_two):
    counts = {}
    string_one = string_one.replace(' ', '')
    string_two = string_two.replace(' ', '')
    if string_one == string_two:
        return True

    for letter in string_one:
        counts[letter] = counts.get(letter, 0) + 1
    for letter in string_two:
        counts[letter] = counts.get(letter, 0) - 1
        if counts[letter] == 0:
            del counts[letter]

    if len(counts) > 2:
        return False
    inc = 0
    for val in counts.values():
        inc += val
    if len(counts) == 2 and inc != 0:
        return False
    if len(counts) == 1 and inc != 1:
        return False
    return True

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
print(one_away("ale", "pale"))
print(one_away("apale", "pale"))
print(one_away("bale", "balz"))
print(one_away("pibb", "pib"))
print()

def string_compression(a_string):
    new_string = []
    cur = a_string[0]
    count = 0
    for i in range(0, len(a_string)):
        if a_string[i] != cur:
            new_string.append(cur)
            new_string.append(str(count))
            cur = a_string[i]
            count = 1
        else:
            count += 1
    new_string.append(cur)
    new_string.append(str(count))
    new_string = ''.join(new_string)

    return new_string if len(new_string) < len(a_string) else a_string

print(string_compression("aabcccccaaa"))
print(string_compression("bbbbccccccccaaaab"))
print(string_compression("aaabbbbcccc"))
print(string_compression("abcdefg"))


def rotate_matrix(matrix, dir):
    pass





def zero_matrix(matrix):
    zeros = []
    # Loop through Rows
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] == 0:
                zeros.append((i, j))

    # For rows
    for e in zeros:
        # for cols
        for row in range(len(matrix)):
            matrix[row][e[1]] =  0

        # for rows
        for col in range(len(matrix[0])):
            matrix[e[0]][col] = 0

    return matrix

test_one = zero_matrix([[3, 4, 1, 5], [4, 2, 2, 0]])
test_two = zero_matrix([[2, 1, 2], [2,3,5], [4,5,6], [7,0,5], [1,2,3], [4,5,6], [1,2,3]])
test_three = zero_matrix([[1,2,3,4], [2,3,4,0], [1,2,3,4], [1,2,3,4]])

print(test_one)
print(test_two)
print(test_three)


def string_rotation(s1, s2):

    if len(s1) != len(s2):
        return False

    s3 = s2 + s2

    if s1 in s3:
        return True
    else:
        return False

print(string_rotation("table", 'bleta'))
print(string_rotation("waterbottle", "erbottlewat"))
print(string_rotation("travel", "velate"))







