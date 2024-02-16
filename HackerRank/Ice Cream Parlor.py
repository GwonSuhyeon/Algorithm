#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    
    # m : money
    
    cost = []
    
    for i in arr:
        if i < m:
            cost.append(i)
    
    cost = sorted(cost)
    
    res1 = -1
    res2 = -1
    
    for i, c in enumerate(cost):
        try:
            find = cost.index(m - c)
            res1 = i
            res2 = find
            break
        except ValueError:
            continue
    
    a = arr.index(cost[res1])
    arr[a] = -1
    
    b = arr.index(cost[res2])
    
    return sorted([a+1, b+1])