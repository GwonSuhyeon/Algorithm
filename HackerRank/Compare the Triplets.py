#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    
    for i in range(len(a)):
        alice_value = a[i]
        bob_value = b[i]
        
        if alice_value > bob_value:
            alice += 1
        elif alice_value == bob_value:
            continue
        else:
            bob += 1
    
    return [alice, bob]