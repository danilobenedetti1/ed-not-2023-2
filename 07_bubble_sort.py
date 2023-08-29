def bubble_sort(lista):
    """
    ALGORITMODE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempe que o
    segundo for MENOR que o primeiro, até que, na última delas,
    nenhuma troca tenha sido realizada.
    """
    # Loop enterno, não sabemos de antemão quantas passadas 
    # serão necessárias
    while True:
        #Controla se houve na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição, pois se chegar na última posição
        # ele não terá um posição para comparar.
        for pos in range(len(lista) -1):
            
            # Se o valor que está a frente na lista (pos + 1) for MENOR
            # do que aquele que está atrás (pos), faz uma TROCA
            if lista[pos + 1] < lista [pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos +1]
                trocou = True #indica que houve troca na passada
        if not trocou: # Não houve troca napassada
            break      # Interrompe o loop eterno