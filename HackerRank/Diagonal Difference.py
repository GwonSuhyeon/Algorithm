#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    first = 0
    second = 0
    max_size = len(arr[0]) - 1
    
    for i, value in enumerate(arr):
        first += value[i]
        second += value[max_size - i]
    
    return abs(first - second)