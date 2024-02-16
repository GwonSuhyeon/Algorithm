#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    time_split = s.split(':')
    res = ''
    
    if 'AM' in s:
        if int(time_split[0]) < 12:
            res = time_split[0] + ':' + time_split[1] + ':' + time_split[2][:2]
        else:
            res = '00' + ':' + time_split[1] + ':' + time_split[2][:2]
    else:
        if time_split[0] == '12':
            res = time_split[0] + ':' + time_split[1] + ':' + time_split[2][:2]
        else:
            res = str(int(time_split[0]) + 12) + ':' + time_split[1] + ':' + time_split[2][:2]
    
    return res