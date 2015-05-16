def xch(str):
    if len(str) <= 1:
        print str
    else:
        mid = str[1:len(str)-1]
        print str[len(str)-1] + mid + str[0]

xch("sample")

