# -*- coding: utf-8 -*-
'''
r == somente leitura
w == escrita (caso o arquivo ja exista, ele sera apgado e um noovo arquivo vazio sera criado)
a == leitura e escrita(adiciona o novo conteudo ao fim do arquivo)
r+ == leitura e escrita
w+ == escrita (o modo w+, assim como o w, tambem apaga o conteudo anterior do arquivo)
a+ == leitura e escrita(abreo arquivo para atualizações)
'''
arquivo = open("arquivo.txt") #abre o arquivo
'''
linhas = arquivo.readlines() 
print("METODO readlines:")
print(linhas) # == ['meu arquivo \n', 'ola mundo']
for x in linhas:
	print(x) # == meu arquivo ola mundo
'''
''' 
print("METODO read: ")
texto_completo = arquivo.read()
print(texto_completo)
'''
'''
w = open("arquivo2.txt", "w") #abre o arquivo metodo W
w.write("Esse é o meu arquivo") #escreve no arquivo
'''
w = open("arquivo.txt", "a") #abre o arquivo metodo A
w.write("Esse é o meu arquivo\n") #escreve no arquivo

w.close()
arquivo.close()