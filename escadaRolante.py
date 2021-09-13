#!/usr/bin/python
# -*- coding: utf-8 -*-

def main(entrada):
	totalPessas = entrada.pop(0)
	l = entrada
	r=10
	for x in range(totalPessas-1):
		r+=l[x+1]-l[x]
	return r


caso1 = [3, 0, 10, 20]
caso2 = [3, 1, 2, 3]
caso3 = [5, 5, 10, 17, 20, 30]

print(main(caso1))