ref_arquivo = open("cadastros.txt","r")

for linha in ref_arquivo:
    valores = linha.split()
    print('QB ', valores[0], valores[1], 'obteve a avaliacao ', valores[10] )

ref_arquivo.close()
