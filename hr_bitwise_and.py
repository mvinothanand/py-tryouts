# in a set of sequential integers from 1 to N, 
# find the max A & B less than K
# where A < B
# Example:
# Set S = {1, 2, 3, 4, 5}, K = 2, then the max A & B less than 2 is 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    integers = {i for i in range(1, N+1)}
    print(f'integers: {integers}')
    max_value = 0
    for i in integers:
        for j in integers:            
            if i < j:
                bitwise_and = i & j  
                print(f'A={i}, B={j}, A&B={bitwise_and}')
                if max_value < bitwise_and < K:
                    max_value = bitwise_and
                    print(f'max value: {max_value}')
    return max_value  

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        print(res)

