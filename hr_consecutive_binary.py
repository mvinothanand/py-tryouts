# Given a base 10 integer, convert it to binary
# Find the max count of consecutive 1s in the binary number
# print the count in base10

def main():
    n = int(input().strip())
    binary_n = bin(n)
    binary_n_str = str(binary_n.replace('0b', ''))
    print(binary_n_str)
    longest_ones = 0
    counter = 1
    for i in binary_n_str:
        if i == '0':
            counter = 0
        else:
            if counter > longest_ones:
                longest_ones = counter
        counter += 1
    print(longest_ones)
            



if __name__ == '__main__':
    main()