# -*- coding: utf-8 -*-
def printT(size, x, y, font, text):
	L = []
	k = 0

	while k < len(text):
		if text[k] == '\n':
			L.append(text[:k])
			text = text[(k+1):]
			k = 0
			if L[-1][0] == " ":
				L[-1] = L[-1][1:]

		else :
			k += 1
	
	L.append(text)
	if L[-1][0] == " ":
		L[-1] = L[-1][1:]
	print(L)


printT(10, 1, 1, "prout", "J'ai fais caca \n c'etait bizare. \n mais j'ai aime ca.")

