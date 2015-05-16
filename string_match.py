def string_match(a, b):
    res = 0
    if len(a) < len(b):
        x = len(a)
    else:
        x = len(b)

    for i in range(x-1):
        if a[i:i+2] == b[i:i+2]:
            res += 1

    print res

string_match('xxcaazz', 'xxbaaz') 
