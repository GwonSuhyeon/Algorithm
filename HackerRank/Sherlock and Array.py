#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    
    left_sum = 0
    right_sum = 0
    
    find = False
        
    
    if len(arr) < 2:
        return 'YES'
    
    if sum(arr[:1]) == 0:
        return 'YES'
    
    if sum(arr[1:]) == 0:
        return 'YES'
    
    right_sum = sum(arr[1:])
    
    for i in range(1, len(arr)):
        
        left_sum += arr[i-1]
        right_sum -= (arr[i])
        
        print(left_sum, right_sum)
        
        if left_sum == right_sum:
            find = True
    
    if find == True:
        return 'YES'
    else:
        return 'NO'