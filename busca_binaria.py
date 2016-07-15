lista = [1,2,3,4,5,6,7,8,9,10]

def busca_bin(x,v):
    inf = 0
    sup = len(v)-1
    while inf <= sup:
        meio = (inf  + sup) // 2
        if v[meio] == x:
            print('encontrado na posicao %i' %(meio))
            return # ou inf = sup +1
        elif v[meio] < x:
            inf = meio + 1
        else:
            sup = meio -1
    print('elemento nao encontrado')

busca_bin(9,lista)

#n de iteracoes 1 + log2n