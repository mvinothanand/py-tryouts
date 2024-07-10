# Given a 6 x 6 array of integers, find the sum of the numbers in
# all hourglasses formed by 3-1-3 structure and return the max sum
# Inpu format: 6 lines each with six space separated values
def main():
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().strip().split())))
        
    print(arr)
    i , j = [0, 0]
    hg_matrix = [3, 3]
    sums = []
    
    while( i + 2 < 6):
        print(f'i is {i}')
        while (j + 2 < 6):
            print(f'j is {j}')
            sums.append(
                arr[i][j] + arr[i][j+1] + arr[i][j+2] + 
                arr[i+1][j+1] + 
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
              )
            j += 1
        i += 1
        j = 0
    
    print(max(sums))


if __name__ == '__main__':
    main()