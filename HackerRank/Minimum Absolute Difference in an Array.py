#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    
    arr = sorted(arr)
    
    minimum = abs((-10**9) - (10**9))
    
    for i in range(len(arr) - 1):
        
        value = abs(arr[i] - arr[i+1])
        
        if value < minimum:
            minimum = value
    
    return minimum