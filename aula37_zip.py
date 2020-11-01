# zip

lista = [1, 2 ,3, 4, 5]
lista2= ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3= ["R$ 2,00", "R$ 5,00", "não tem preço", "não tem preço", "R$ 2,00"]

for numero, nome, valor in zip(lista, lista2, lista3):
	print(numero, nome, valor)