#!/usr/bin/python

i = raw_input().split()

out = float(i[0])
full = float(i[1])

if (out % 5 == 0.0) and (out + 0.5 <= full):
    full = full - out - 0.50

print("%.2f" % full)
