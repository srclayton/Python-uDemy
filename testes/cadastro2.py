# -*- coding: utf-8 -*-
arquivo_original = open("cadastros.txt", "r")
arquivo_copia = open("cadastros2.txt", "w")
for linha in arquivo_original:
	valores = linha.split()
	count=0
	while count < 11:
		arquivo_copia.write(valores[count] + " ")
		count+=1
	arquivo_copia.write("\n")

busca = valores.find("Colt")
print(busca + "passei")