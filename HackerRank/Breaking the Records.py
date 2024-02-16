#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    
    n = len(scores)
    
    minimum = 0
    maximum = 0
    
    Min_cnt = 0
    Max_cnt = 0
    
    for i in range(n):
        
        if i == 0:
            minimum = scores[i]
            maximum = scores[i]
            continue
        
        if scores[i] < minimum:
            minimum = scores[i]
            Min_cnt += 1
        elif scores[i] > maximum:
            maximum = scores[i]
            Max_cnt += 1
    
    return [Max_cnt, Min_cnt]