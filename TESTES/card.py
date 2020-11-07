# -*- coding: utf-8 -*-
def verifica_operadora(num_card):
	if num_card[0:2] == "34" or num_card[0:2] == "37" or num_card[0:2] == "38" or num_card[0:2] == "30" or num_card[0:2] == "36" or num_card[0:2] == "51" or num_card[0:2] == "52" or num_card[0:2] == "53" or num_card[0:2] == "54" or num_card[0:2] == "55" or num_card[0:2] == "4" or num_card[0:2] == "6011" or num_card[0:2] == "2014" or num_card[0:2] == "2149" or num_card[0:2] == "3" or num_card[0:2] == "2131" or num_card[0:2] == "1800":
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
	impar_par = 0
	new_num=0
	aux=0
	#FALTA COMEÇAR PELO FINAL
	while i < tamanho:
		aux= int(num_aux[i])
		if impar_par % 2 == 0:
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
	print(resultado)
	if valida_soma(resultado):
		if operadoras[num_aux[0]]:
			print(num_aux + " " + operadoras[num_aux[0]] + " valido!")
		elif operadoras[num_aux[0:2]]:
			print(num_aux + " " + operadoras[num_aux[0:2]] + " valido!")
		else:
			print(num_aux + " " + operadoras[num_aux[0:4]] + " valido!")
	else:
		if operadoras[num_aux[0]]:
			print(num_aux + " " + operadoras[num_aux[0]] + " invalido!")
		elif operadoras[num_aux[0:2]]:
			print(num_aux + " " + operadoras[num_aux[0:2]] + " invalido!")
		else:
			print(num_aux + " " + operadoras[num_aux[0:4]] + " invalido!")
operadoras={"51":"Mastercard","52":"Mastercard","53":"Mastercard","54":"Mastercard","55":"Mastercard","4":"Visa", "34":"Amex", "37":"Amex", "30":"Diners", "36":"Diners", "38":"Diners", "6011":"Discover", "2014":"enRout", "2149":"enRout", "3":"JCB", "2131":"JCB", "1800":"JCB"}
numero_cartao = int(input("Informe o numero do cartão: "))
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
