def front3(str):
    if len(str) <= 3:
        print str * 3
    else:
        print str[0:3] * 3


front3("test")
