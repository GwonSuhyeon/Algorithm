#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    
    apple_cnt = 0
    orange_cnt = 0
    
    for i in range(len(apples)):
        land = apples[i] + a
        
        if s <= land and land <= t:
            apple_cnt += 1
    
    for i in range(len(oranges)):
        land = oranges[i] + b
        
        if s <= land and land <= t:
            orange_cnt += 1
    
    print(apple_cnt)
    print(orange_cnt)