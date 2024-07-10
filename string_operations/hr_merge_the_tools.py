# A string 's' of size 'n' and an integer 'k' (a factor of n) are given
# Find substrings from 's' each of length n/k
# From the substrings remove duplicate occurences of letters
#     and print the sequence in same order
# Example: s = 'XXXYHJGGY' k = 3 --> 'X', 'YHJ', 'GY'

def main():
    string = 'AABCAAADA'
    n = len(string)
    k = 3
    substrings = []
    # substr = set('YHJ')
    # print(substr)
    # print(''.join(substr))
    # print(repr(substr).removeprefix('{').removesuffix('}'))
    start_pos = 0
    for i in range(k, n + 1, k):
        substr_1 = string[start_pos:i]
        # print(substr_1)        
        substr_2 = ''

        for j in range(k):
            if substr_1[j] not in substr_2:
                substr_2 += substr_1[j]
        
        start_pos = i
        print(substr_2)        


if __name__ == '__main__':
    main() 