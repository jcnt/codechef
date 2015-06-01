#!/usr/bin/python
#
# input
# 4
# 1
# 2
# 5
# 3

a = int(raw_input())

for i in range(a):
    res = 1
    inc = 1
    curr = int(raw_input())
    for j in range(curr):
        res = res * inc
        inc += 1
    print res

