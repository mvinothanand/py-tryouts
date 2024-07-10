#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    # Method - 1
    print('by method 1')
    for i in range(1, len(arr) + 1):
        print(arr[-1 * i], end=' ')

    print()

    # Method 2
    print('by method 2')
    print(*arr[::-1])
    