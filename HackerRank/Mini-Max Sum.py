#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    min_value = min(arr)
    max_value = max(arr)
    
    sum_value = sum(arr)
    
    print(f'{sum_value - max_value} {sum_value - min_value}')