#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    if x1 <= x2 and v1 <= v2:
        return 'NO'
        
    if ((x1 - x2) / (v2 - v1)) % 1 == 0:
        return 'YES'
    else:
        return 'NO'