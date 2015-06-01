#!/usr/bin/python
#
#

a = int(raw_input())
l = []

for i in range(a):
    l.append(int(raw_input()))

l.sort()

for i in range(a):
    print l[i]

