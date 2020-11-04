# -*- coding: utf-8 -*-
def verifica_operadora(num_card):
	if num_card[0:2] == "49" or num_card[0:2] == "37" or num_card[0:2] == "38" or num_card[0:2] == "30" or num_card[0:2] == "34" or num_card[0:2] == "51" or num_card[0:2] == "55":
		return True 
	else:
		return False
def soma(x):
	aux= str(x)
	soma=0
	for i in aux:
		y = int(i)
		soma=soma+y
	return soma
def valida_soma(soma_final):
	if soma_final % 10 == 0:
		return True
	else:
		return False
def luhn(num_card,num_aux,tamanho):
	i = 0
	impar_par = 0
	new_num=0
	aux=0
	while i < tamanho:
		aux= int(num_aux[i])
		if impar_par % 2 == 1:
			aux= aux * 2
			if aux > 9:
				new_num = (new_num * 100) + aux
			else:
				new_num = (new_num * 10) + aux
		else:
			new_num = (new_num * 10) + aux
		impar_par+=1
		i+=1
	resultado = soma(new_num)
	if valida_soma(resultado):
		print(num_aux + " " + operadoras[num_aux[0:2]] + " valido!")
	else:
		...
	

operadoras={"51":"Mastercard","52":"Mastercard","53":"Mastercard","54":"Mastercard","55":"Mastercard"}

numero_cartao = int(input("Informe o numero do cartão: "))
num_aux = str(numero_cartao)
teste=int(num_aux[1])
tamanho = len(num_aux)
if tamanho > 2 and tamanho < 17:
	operadora = verifica_operadora(num_aux)
	if operadora:
		luhn(numero_cartao,num_aux,tamanho)
	else:
		print(num_aux + " Operadora desconhecida!")
else:
	if tamanho < 13:
		print("O numero é muito curto!")
	else:
		print("O numero é muito longo!")
