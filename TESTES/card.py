# -*- coding: utf-8 -*-
def verifica_operadora(num_card):
	if num_card[0:2] == "36" or num_card[0:2] == "37" or num_card[0:2] == "38" or num_card[0:2] == "30" or num_card[0:2] == "34" or num_card[0:2] == "51" or num_card[0:2] == "55":
		return True 
	else:
		return False
def luhn(num_card,num_aux,tamanho):
	soma=0
	i=0
	par_impar=0
	num_aux = list(str(num_aux))
	print(num_aux)
	while i < tamanho:
		if par_impar % 2 == 1:
			num_aux[i] = num_aux[i] + 2
		print(num_aux[i])
		i+=1
		par_impar+=1


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
