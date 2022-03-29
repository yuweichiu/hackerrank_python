#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    max_sum = 0
    n = int(len(matrix[0])/2)
    for i in range(n):
        for j in range(n):
            poss = [matrix[i][j], matrix[2*n-i-1][j], matrix[i][2*n-j-1], matrix[2*n-i-1][2*n-j-1]]
            max_sum += max(poss)
    return max_sum

if __name__ == '__main__':
    matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    # >>> 414