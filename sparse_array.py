#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    str_dict = {}
    keys = set(strings)
    for k in keys:
        str_dict[k] = 0
        
    for s in strings:
        str_dict[s] += 1
        
    results = []
    for q in queries:
        if q not in keys:
            results += ['0']
        else:
            results += [str(str_dict[q])]
    
    return results
        

if __name__ == '__main__':
    strings = ['ab', 'ab', 'abc']
    queries = ['ab', 'abc', 'bc']
    res = matchingStrings(strings, queries)
