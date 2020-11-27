# -*- coding: utf-8 -*-
def verifica_operadora(num_card):
	if num_card[0:2] == "34" or num_card[0:2] == "37" or num_card[0:2] == "38" or num_card[0:2] == "30" or num_card[0:2] == "36" or num_card[0:2] == "51" or num_card[0:2] == "52" or num_card[0:2] == "53" or num_card[0:2] == "54" or num_card[0:2] == "55":
		return True
	elif num_card[0] == "4" or num_card[0]== "3":
		return True
	elif num_card[0:4] == "6011" or num_card[0:4] == "2014" or num_card[0:4] == "2149" or num_card[0:4] == "2131" or num_card[0:4] == "1800":
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
	impar_par = 1
	new_num=0
	aux=0
	while tamanho > 0:
		aux= int(num_aux[tamanho-1])
		if impar_par % 2 == 0:
			aux= aux * 2
			if aux > 9:
				new_num = (new_num * 100) + aux
			else:
				new_num = (new_num * 10) + aux
		else:
			new_num = (new_num * 10) + aux
		impar_par+=1
		tamanho-=1
	resultado = soma(new_num)
	print(resultado)
	#falta verificar o tamanho do cartão para verificar a operadora. ex de input = 378282246310005   output: JCB, ao invez de amex
	if valida_soma(resultado):
		if num_aux[0] in operadoras:
			print(num_aux + " " + operadoras[num_aux[0]] + " valido!")
		elif num_aux[0:2] in operadoras:
			print(num_aux + " " + operadoras[num_aux[0:2]] + " valido!")
		else:
			print(num_aux + " " + operadoras[num_aux[0:4]] + " valido!")
	else:
		if num_aux[0] in operadoras:
			print(num_aux + " " + operadoras[num_aux[0]] + "invalido!")
		elif num_aux[0:2] in operadoras:
			print(num_aux + " " + operadoras[num_aux[0:2]] + " invalido!")
		else:
			print(num_aux + " " + operadoras[num_aux[0:4]] + " invalido!")
operadoras={"51":"Mastercard","52":"Mastercard","53":"Mastercard","54":"Mastercard","55":"Mastercard","4":"Visa", "34":"Amex", "37":"Amex", "30":"Diners", "36":"Diners", "38":"Diners", "6011":"Discover", "2014":"enRout", "2149":"enRout", "3":"JCB", "2131":"JCB", "1800":"JCB"}
numero_cartao=1
while numero_cartao != 0:
	numero_cartao = int(input("Digite o numero do cartão sem pontos ou espaços, ou digite 0 para sair \n"))
	if numero_cartao != 0:
		num_aux = str(numero_cartao)
		tamanho = len(num_aux)
		if tamanho > 12 and tamanho < 17:
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
