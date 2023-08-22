# Lista de frutas
frutas = ["Laranja", "maça", "uva", "pera", "mamão", "abacate","amora"]

# Para percorrer uma lista e exibir apenas seus elementos,
#usamos a estrutura for..in, como já vimos no arquivo n.02

for f in frutas:
    print(f)

print('-' * 40) #traço

# Imprimindo uma lista de trás paraafrente: reversed()

for x in reversed(frutas):
    print(x)

print('-' * 40)#traço

# No entanto, frequentemente precisamos exibir, além do
# valor do elemento, também sua posição.Neste caso devemos
# usar a estrutura fpr..in combinada com as funções rang() e
# e len()

for pos in range(len(frutas)):
    #print(frutas[pos], ":", pos) 
    #print("A fruta", frutas[pos], "está na posição", pos, ".")   
    print(f"A fruta {frutas[pos]} está na posição {pos}.")


print('-' * 40)#traço

# Às vezes, é necessário percorrer a lista de trás para frente,
# mas tendo acesso também à posição dos elementos. Para isso,
# usamos a estrutura for..in, range() com três parametros e len()

for i in range(len(frutas) -1, -1, -1):
    print(f"A fruta {frutas[i]} está na posição {i}.")


print('-' * 40)#traço