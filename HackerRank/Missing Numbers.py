#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    
    # for i in arr:
    #     brr.remove(i)
    # return sorted(brr)
    
    a_q = deque()
    b_q = deque()
    
    arr = sorted(arr)
    brr = sorted(brr)
    
    missing = []
    
    for i in arr:
        a_q.append(i)
    
    for i in brr:
        b_q.append(i)
    
    for i in range(len(brr)):
        
        if len(a_q) == 0:
            while len(b_q) != 0:
                b = b_q.popleft()
                
                if b not in missing:
                    missing.append(b)
            
            break
        
        a = a_q.popleft()
        b = b_q.popleft()
        
        if a != b:
            a_q.appendleft(a)
                        
            if b not in missing:
                missing.append(b)

    
    return missing