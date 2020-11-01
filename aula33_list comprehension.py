# list comprehension 

x = [1, 2, 3, 4, 5]
#y = [valor_a_adicionar laço condição]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]
'''

print("Usando list comprehension")
print(x)
print(y)
'''
print(z)