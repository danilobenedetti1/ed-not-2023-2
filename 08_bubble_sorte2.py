comps = trocas = passd = 0


def bubble_sort(lista):
    """
    ALGORITMODE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempe que o
    segundo for MENOR que o primeiro, até que, na última delas,
    nenhuma troca tenha sido realizada.

    ESTA VERSÃO TEM UMA PEQUENA OTIMIZAÇÃO QUE VAI DIMINUINDO A
    QUANTIDADE DE COMPARAÇÕES A CADA PASSADA
    """
    # Wusando as variáveis globaix
    global comps,trocas, passd
    comps = trocas = passd = 0

    # Loop enterno, não sabemos de antemão quantas passadas 
    # serão necessárias
    while True:

        #Início de uma nova passada
        passd +=1

        #Controla se houve na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição, NA PRIMEIRA PASSADA
        # Nas demais passadas, o percurso vai diminuindo uma posição
        for pos in range(len(lista) -passd):
            
            # Se o valor que está a frente na lista (pos + 1) for MENOR
            # do que aquele que está atrás (pos), faz uma TROCA
            if lista[pos + 1] < lista [pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos +1]
                trocou = True #indica que houve troca na passada
                trocas += 1

        # O if representa uma comparação
            comps +=1

        if not trocou: # Não houve troca napassada
            break      # Interrompe o loop eterno
 #############################################################################################   
# nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]
# melhor caso
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# pior caso
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    
print("Antes: ", nums)
bubble_sort(nums)
print("DEPOIS: ", nums) 
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

#########################################################

#TESTE COMO ARQUIVO DE 1 M+ NOMES

# import sys
# sys.dont_write_bytecode = True # Impede a criação do cache

# # Importando a lista de nomes
# from data.nomes_desord import nomes
# from time import time

# nomes10000 = nomes[:10000]

# hora_ini = time()
# bubble_sort(nomes10000)
# hora_fim = time()
# print(nomes10000) # Lista após ordenação
# print(f"Tempo gato: {(hora_fim -hora_ini) * 1000} * ms\n")