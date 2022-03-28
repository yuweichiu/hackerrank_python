#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alphabet_list = [0] * 26
    for alp in s:
        ascii = ord(alp)
        if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
            if ascii >= 97:
                ascii -= (32+65)
            else:
                ascii -= 65
            alphabet_list[ascii] += 1
    
    for i in alphabet_list:
        if i == 0:
            return "not pangram"
    
    return "pangram"


pangrams("We promptly judged antique ivory buckles for the next prize")
# >>> 'pangram'