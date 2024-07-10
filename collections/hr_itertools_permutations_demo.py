# the permuations method in the itertools module,
# will return all permutations of the iterable elements
# of length 'r' or the iterable length.
# If the iterable is lexicographically ordered, then the permuations
# are also ordered lexicographical.

from itertools import permutations

def main():
    print(permutations([1, 2, 3, 4]))

    print(list(permutations([1, 5, 6, 8], 2)))

    print(list(permutations('abc', 2)))


if __name__ == '__main__':
    main()