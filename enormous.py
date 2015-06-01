#!/usr/bin/python
import sys

l = sys.stdin.readlines()
f = l[0].split()
res = 0

for i in range(len(l)-1):
    if int(l[i+1]) % int(f[1]) == 0:
        res +=1
print res

