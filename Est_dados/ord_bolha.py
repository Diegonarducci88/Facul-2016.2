lista = [50,6,5,4,3,7,33,2,1]

def ord_bolha(v):
    for i in range(len(v)):
        bolha = i
        while bolha > 0:
            if v[bolha] < v[bolha-1]:
                auxiliar = v[bolha-1]
                v[bolha-1] = v[bolha]
                v[bolha] = auxiliar
                bolha = bolha - 1
            else:
                bolha = 0
    print(v)

ord_bolha(lista)

