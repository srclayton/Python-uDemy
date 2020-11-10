# -*- coding: utf-8 -*-
arquivo = open("cadastros3.txt", "a")
arquivo_leitura = open("cadastros3.txt", "r")
def menu():
	print("===================================")
	print("'        SISTEMA DE CADASTRO      '")
	print("===================================")
def cadastrar():
	tab = "		"
	nasc= input("\nDigite a data de nascimento: ")
	cpf= input("\n Digite o cpf: ")
	tel= input("\nDigite o numero de telefone")
	arquivo.write(nome + tab + nasc + tab + cpf + tab + tel + '\n')
	
menu()
chose= input("Digite 'Cad' p/ cadastrar ou 'Find' para localizar: ")
nome= input("\nDigite o nome: ")
if chose == "Cad":
	cadastrar()
else:
	count=0
	for linha in arquivo_leitura:
		valores= linha.split()
		if valores[0] == nome:
			print('Nome: '+ valores[0] + ' CPF: ' + valores[2] + ' Telefone: ' + valores[3])
			bool= False
			break
	if bool:
		print('Nome não encontrado!')
		chose= input("Deseja cadastrar um novo ? y/n")
		if chose=="y" or chose=="Y":
			nome= input("\nDigite o nome: ")
			cadastrar()

arquivo.close()
arquivo_leitura.close()