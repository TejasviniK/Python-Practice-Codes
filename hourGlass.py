#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -10000
    for row in range(4):
        for col in range(4):
            num = 0
            sum = 0
            for i in range(row, row+3):
                for j in range(col , col+3):
                    if(num == 3 or num == 5):
                        print(" ", end= " ")ssss
                        num += 1
                    else:
                        print(arr[i][j], end=" ")
                        num += 1
                        sum = sum + arr[i][j]
                print("")
            print("sum", sum)
            if(sum > max_sum):
                max_sum = sum
                print("max_sum", max_sum)
    print(max_sum)