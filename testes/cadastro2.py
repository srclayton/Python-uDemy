# -*- coding: utf-8 -*-
arquivo_original = open("cadastros.txt", "r")
arquivo_copia = open("cadastros2.txt", "a")
#for linha in arquivo_original:
#	valores = linha.split()
#	count=0
#	while count < 11:
#		arquivo_copia.write(valores[count] + " ")
#		count+=1
#	arquivo_copia.write("\n")
arquivo_2 = open("cadastros2.txt" , "r")
nome = input("Digite o nome:")
for i in arquivo_2:
	valores = i.split()
	if valores[0] == nome:
		print(valores[0] + " ACHEI \n")
		
print(valores[0])
print("Nome não encontrado!")
chose= input("Deseja cadastrar um novo nome? y/n")
if chose == "y" or chose =="Y":
	arquivo_copia.write(nome + " ")
		
arquivo_copia.close()
arquivo_original.close()
arquivo_2.close()