import sys
import math

inf = 10000000
n = int(raw_input())

power = [];

for i in xrange(n):
    pi = int(raw_input())
    power.append (pi)
power.sort()
i = 0
while i < n-1:
    tmp = power[i+1] - power[i]
    if tmp < inf:
        inf = tmp
    i+=1
    
print inf