def interpretCashier(inpt):
    if inpt.isdigit():
        return "PIN"
    elif '.' in inpt:
        list1 = inpt.split('.')
        print(list1)
        if len(list1) == 2:
            for l in list1:
                if l.isdecimal():
                    	return "Transaction"
        else :
            return "Password"
    else :
        return "Password"


print(interpretCashier("12..34..56"))
print(interpretCashier("123456"))
print(interpretCashier("my$up3rs3cur3p4$$w0rd"))