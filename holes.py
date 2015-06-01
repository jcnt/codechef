#!/usr/bin/python
#
# input
# 2
# CODECHEF
# DRINKEATCODE
#

a = int(raw_input())

for i in range(a):
    res = 0
    word = raw_input()
    for k in range(len(word)):
        if word[k] in "ADOPQR":
            res += 1
        elif word[k] == "B":
            res += 2
    print str(res)


