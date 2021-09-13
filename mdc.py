# -*- coding: utf-8 -*-

def mdc(num1, num2):
	resto = None
	while resto is not 0:
		resto = num1 % num2
		num1  = num2
		num2  = resto
	return num1

a = int(input("Digite o A: "))
b = int(input("Digite o B: "))

print(mdc(a, b))
