def sortString(the_string):
    if not isinstance(the_string, str) :
        return "Not a string!"
    else :
        capitalStr = ""
        lowerStr = ""
        spclStr = ""
        spaceCount = 0
        for s in the_string :
            if ord(s) >= 65 and ord(s) <= 90 :
                capitalStr += s
            elif ord(s) >= 97 and ord(s) <= 122:
                lowerStr += s
            elif ord(s) >= 33 and ord(s) <= 64:
                spclStr += s
            else :
                spaceCount += 1
        return capitalStr+"\n"+lowerStr+"\n"+spclStr+"\n"+str(spaceCount)

print(sortString("ZOMG Hello, CS1301!!"))
print(sortString(5))
