#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    a1, a2, a3 = map(sum, (h1, h2, h3))
    while h1 and h2 and h3:
        if a1 == a2 == a3:
            return a1

        m = min(a1, a2, a3)

        while a1 > m:
            a1 -= h1.pop(0)
        while a2 > m:
            a2 -= h2.pop(0)
        while a3 > m:
            a3 -= h3.pop(0)

    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
