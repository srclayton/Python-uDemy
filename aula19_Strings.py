# -*- coding: utf-8 -*-

a = "Clayton"
b = "Kamila"

concatenar = a + " " + b + "\n"
tamanho = len(concatenar) #Pega o tamanho da string
print("somente a 2° posição : "+ a[2]) #Acessa e print a posição 2 da variavel a
print("somento o intervalor [x,y] da string: " +concatenar[0:7])#Acessa e printa o intervalo [x,y] na vareavel.
print("metodo .lower: " +concatenar.lower())#printa a string em minusculo
print("metodo .upper: " +concatenar.upper())#printa a string em maiusculo
concatenar = concatenar.upper()#atribui a todas as letras caixa alta
print("upper atribuido: " + concatenar)
print("metodo strip: " +concatenar.strip()) #remove caracteres especiais e espaços

minha_string = "o rato roeu a roupa do rei de roma"
minha_lsita = minha_string.split("r")#cria uma lista diferente a cada caracter definido
print(minha_lsita)

busca = minha_string.find("rei")#.find localiza uma palavra na string e retorna sua localização, caso não encontre retornara -1
print(busca)
print(minha_string[busca:])

minha_string = minha_string.replace("o rei", "a rainha")#localiza e troca o conteudo da string
print(minha_string)
