def get_capitals(the_string):
    capStr = ""
    for s in the_string :
        if ord(s) >= 67 and ord(s) <= 90:
            capStr += s
    return capStr
    
print(get_capitals("CS1301"))
print(get_capitals("Georgia Institute of Technology"))
