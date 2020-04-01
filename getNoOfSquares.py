def getNoOfSquares(min, max):
    d = int(max/min)
    q = max%min #1
    r = max-(min*d) #1
    #if(r > min):
    #   max = r
    #else :
    max = min
    min = r
    #min = q #1
    if (min == 0):
        return d
    else:
        #print(min, max)
        squares = d + getNoOfSquares(min, max)
        #print(squares)
        return squares

print("No of squares: ", getNoOfSquares(2, 7) )
