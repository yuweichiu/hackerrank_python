#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length = len(arr)
    pos_cnt = 0
    neg_cnt = 0
    zero_cnt = 0
    for i in arr:
        if i == 0:
            zero_cnt += 1
        elif i < 0:
            neg_cnt += 1
        else:
            pos_cnt += 1
    print('{0:1.6f}'.format(pos_cnt/length))
    print('{0:1.6f}'.format(neg_cnt/length))
    print('{0:1.6f}'.format(zero_cnt/length))
    
    return None

if __name__ == '__main__':
    arr = [1, 1, 0, -1, -1]
    plusMinus(arr)