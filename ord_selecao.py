lista = [30,20,100,10,40]

def ord_selecao(v):
    for i in range(len(v)):
        menor = i
        for j in range(i+1,len(v)):
            if v[j] < v[menor]:
                menor = j
        auxiliar = v[i]
        v[i] = v[menor]
        v[menor] = auxiliar

    print(v)

ord_selecao(lista) 
