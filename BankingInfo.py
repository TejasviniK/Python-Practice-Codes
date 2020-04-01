input_string = "1234"
if input_string.isdigit():
    print("PIN")
elif '.' in input_string:
    list1 = input_string.split('.')
    print(list1)
    if len(list1) == 2:
        for l in list1:
            if l.isdecimal():
               	print("Amount")
    else :
        print("Password")
else :
        print("Password")