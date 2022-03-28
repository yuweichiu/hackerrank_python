#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    total_sum = 0
    for a in arr:
        total_sum += a
        
    for i in range(len(arr)):
        sub_sum = total_sum - arr[i]
        if i == 0:
            max_sum = min_sum = sub_sum
        else:
            if sub_sum > max_sum:
                max_sum = sub_sum
            if sub_sum < min_sum:
                min_sum = sub_sum
    
    print('{0:d} {1:d}'.format(min_sum, max_sum))
        

if __name__ == '__main__':

    arr = [1, 3, 5, 7]

    miniMaxSum(arr)