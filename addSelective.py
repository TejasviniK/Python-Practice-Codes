list1 =  [ 1, 2 , 3, 4, 6, 3, 4, 5, 9, 1, 2, 3, 4, 6, 1, 9, 2]
print(list1)
i = 0
sum = 0
while i < len(list1) :
    if list1[i] == 6 :
        while not (list1[i] == 9) :
            i += 1
        if i < len(list1) - 1 :
            i += 1
        else :
            break
    sum += list1[i]
    print(list1[i])
    i += 1
print("sum : ", sum)







# 1, 2 , 3, 4, 6, 3, 4, 5, 9, 1, 2