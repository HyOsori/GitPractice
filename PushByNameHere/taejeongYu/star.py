# -*- coding: euc-kr -*-
# BaekJoon/10991
def star(n):
    for i in range(1, n+1) :
        output = ' ' * (n - i)
        NoS = 1
        while NoS < 2 * i + 1:
            if NoS % 2 == 1:
                output += '*'
            else :
                output += ' '
            NoS += 1
        i += 1
        print(output) 

star(int(input()))