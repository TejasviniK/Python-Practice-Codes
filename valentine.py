for i,j in zip(range(5,0,-1), range(0,13,2)):
    #print(i, j)
    if(j == 0) :
        print(" " * i + "*" + " " * j)
    else:
        print(" "*i+"*"+" "*j+"*")
    if(i == 1) :
        k = int(j/2)
        #print(k)
        print(" "*i+"*"+" "*k+"*"+" "*k+"*")



