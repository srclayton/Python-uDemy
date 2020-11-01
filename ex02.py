# -*- coding: utf-8 -*- 
p_nota = float(input("Digite a primeira nota: "))
s_nota = float(input("Digite a segunda nota: "))
media = (p_nota + s_nota) / 2
if media > 6:
	print("Parabéns, você esta acima da média")
else:
	print("Oh não, você esta abaixo da média")