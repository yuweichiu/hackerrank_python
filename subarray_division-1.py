#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    # 0, 1, 2, 3, 4
    nways = 0
    for i in range(len(s)):
        if m == 1:
            sub_arr = [s[i]]
        elif i+m <= len(s):
            sub_arr = s[i: i+m]
        elif m > len(s):
            return 0
        else:
            return nways
            
        sub_sum = sum(sub_arr)
        if sub_sum == d:
            nways += 1
            
    return nways
            
        

if __name__ == '__main__':
    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2
    birthday(s, d, m)

