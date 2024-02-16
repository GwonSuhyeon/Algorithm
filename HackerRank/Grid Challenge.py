#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    
    grid_sort = []
    
    res = True
    
    for i in range(len(grid)):
        grid_sort.append(sorted(grid[i]))
    
    for i in range(len(grid_sort[0])):
        for k in range(len(grid_sort) - 1):
            
            if grid_sort[k][i] > grid_sort[k+1][i]:
                res = False
    
    if res == True:
        return 'YES'
    else:
        return 'NO'