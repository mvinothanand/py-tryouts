# Sort the given list of numbers by repeatedly swapping positions until
# the iteration with no swaps

def main():
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    swaps = 0
    swapoccured = True
    while swapoccured:
        swapoccured = False
        for i in range(len(a)-1):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                swaps += 1
                swapoccured = True

    print(f'Array is sorted in {swaps} swaps')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    print(f'Sorted array is {a}')



if __name__ == '__main__':
    main()