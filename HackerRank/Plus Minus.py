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
    
    n = len(arr)
    positive = 0
    negative = 0
    zero = 0
    
    for value in arr:
        
        if value < 0:
            positive += 1
        elif value == 0:
            zero += 1
        else:
            negative += 1
    
    print('%.6f' %(negative / n))
    print('%.6f' %(positive / n))
    print('%.6f' %(zero / n))