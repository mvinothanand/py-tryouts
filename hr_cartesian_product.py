# use the itertools.product to get the cartesian product of two lists
from itertools import product

def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for item in product(A, B):
        print(item, end= ' ')
        

if __name__ == '__main__':
    main()