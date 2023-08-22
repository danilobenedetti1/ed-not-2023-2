def busca_sequencial(lista, val):
    """
    Função que realiza uma busca sequencial em uma lista
    procurando por val.
    Se val for encontrado, retorna a posição de val na Lista.
    Caso contrário, retorna o valor convencional -1.
    """
    #Percorre a lista do incício ao fim usando range() e lenc()
    #(precisamos ter acesso às posições dos elementos)
    for pos in range(len(lista)):
        #Enctrou val; retorna a posição onde foi encontrado
        if val == lista[pos] : return pos
    #<-- cuidado com a indentaçãoaqui
    #percorreu toda a lista e não encontrou val: retorna -1
    return -1
###################################################################

# Para a busca sequencial, a lista NÃO PRECISA estar ordenada
nums = [9, 21,33,12,0, -3, 30, -15, 6, 3, 27]

# EXEMPLOS
pos30 = busca_sequencial(nums,30)
pos_menos3 = busca_sequencial(nums, -3)
pos19 = busca_sequencial(nums,19)

print(nums)
print(f"Elemento 30 encontrado na posição {pos30},")
print(f"Elemento -3 encontrado na posição {pos_menos3},")
print(f"Elemento 19 encontrado na posição {pos19},")