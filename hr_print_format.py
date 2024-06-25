# Given an integer N, for each number from 1 to N,
# print the decimal, octal, hexadecimal and binary equivalents
# each number should be on a newline with each value single space
# separated and the width as per the binary value
# Example: Input 17
# Output:
#   1     1     1     1
#   2     2     2    10
#   3     3     3    11
#   4     4     4   100
#   5     5     5   101
#   6     6     6   110
#   7     7     7   111
#   8    10     8  1000
#   9    11     9  1001
#  10    12     A  1010
#  11    13     B  1011
#  12    14     C  1100
#  13    15     D  1101
#  14    16     E  1110
#  15    17     F  1111
#  16    20    10 10000
#  17    21    11 10001

def main():
    # input_integer = int(input())
    input_integer = 17

    # the largest integer will have the max bin length
    max_width = len(format(input_integer, 'b'))

    # Store the values in a list of lists
    for i in range(1, input_integer + 1):
        binary_value = bin(i).lstrip('0b') 
        print(
                str(i).rjust(max_width), 
                oct(i).lstrip('0o').rjust(max_width), 
                hex(i).lstrip('0x').upper().rjust(max_width), 
                binary_value.rjust(max_width)
        )
    
if __name__ == '__main__':
    main()
