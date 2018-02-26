import sys
import math

while True:
    max=0
    p = 0
    for i in xrange(8):
        m = int(raw_input())
        if m > max :
            max = m
            p = i
    print p