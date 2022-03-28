#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hrs = s[0:2]
    mm_ss = s[2:-2]
    am_pm = s[-2:]
    if am_pm == 'AM' and hrs == '12':
        new_hrs = '00'
    elif am_pm == 'PM' and hrs != '12':
        new_hrs = '{0:2d}'.format(int(hrs) +12)
    else:
        new_hrs = hrs
        
    return new_hrs + mm_ss


if __name__ == '__main__':
    result = timeConversion("07:05:45PM")
    # >>> 19:05:45