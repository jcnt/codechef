def string_splosion(str):
    a = ""
    for i in range(len(str)+1):
        a = a + str[0:i]
    print a

string_splosion("ei")
