from itertools import permutations

def main():
    iterable, r = input().split()
    permutation_length = int(r)

    items = list(permutations(sorted(iterable), permutation_length))
    print(items)

    for item in items:
        print(''.join(item))


if __name__ == '__main__':
    main()