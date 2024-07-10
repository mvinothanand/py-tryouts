# Find the average of distinct values
# result should be rounded to 3 decimals

def main():
    # size of the array
    #N = int(input())
    N = 10

    # N integers in a space separated string
    #arr = list(map(int, input().split()))
    arr = list(map(int, '161 182 161 154 176 170 167 171 170 174'.split()))

    # unique integers
    distinct_values = set(arr)

    #average
    avg = sum(distinct_values) / len(distinct_values)

    print(round(avg, 2))



if __name__ == '__main__':
    main()