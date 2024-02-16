#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    
    maximum = max(candles)
    cnt = 0
    
    for i in range(len(candles)):
        
        if candles[i] == maximum:
            cnt += 1
    
    return cnt