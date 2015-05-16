def lasttwo(str):
    i = 0 
    for j in range(len(str[:-2])):
        if str[j:j+2] == str[-2:]:
            i += 1

    print i



lasttwo("axxaaaxxaxx")

