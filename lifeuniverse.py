#
# input
#
# 8
# 22
# 42
# 

import sys

i = sys.stdin.readlines()

for x in  range(0, len(i)):
    if int(i[x]) == 42:
        break
    else:
        print int(i[x])

