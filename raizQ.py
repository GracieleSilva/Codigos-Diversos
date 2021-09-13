# -*- coding: utf-8 -*-

def RaizQ(x): 
    if (x == 0 or x == 1): 
        return x 
    i = 1; result = 1
    while (result <= x): 
        i += 1
        result = i * i 
    return i - 1

x = int(input("Digite o valor de x: "))
print(RaizQ(x)) 