#!/bin/python3

import os


#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    pass


#
# Write your code here.
#

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
