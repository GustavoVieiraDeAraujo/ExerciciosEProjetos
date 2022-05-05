def mediana_e_mais_proximo_media_e_pos(lista_1):
    lista=sorted(lista_1)
    tam = len(lista)
    if tam > 0:
        if tam % 2 == 0:
            mediana = (lista[int(tam/2)] + lista[int(tam/2-1)])/2
        else:
            mediana = (lista[int(tam/2)])
        somador = 0
        for i in lista:
            somador += i
        media = somador/tam
        delta = lista[tam-1] - lista[0]
        prox_media = lista[0]
        for i in lista:
            if abs(media-i) < delta:
                prox_media = i
                delta = media - i
                posicao = lista_1.index(i)
    else:
        prox_media = None
        mediana = None
        posicao = None
    return mediana, prox_media, posicao