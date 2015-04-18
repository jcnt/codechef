def miss(str, x):
    f = []
    for i in range(0, len(str)):
        if i != x:
          f.append(str[i])
    print "".join(f)


miss("kitten", 3)
