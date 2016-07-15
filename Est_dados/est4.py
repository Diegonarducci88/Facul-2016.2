def busca1(x,v):
    i = 0
    while i < len(v):
        if v[i] == x:
            #print('valor encontrado na posicao %i'%(i))
            return i
        else:
            i += 1
    return -1


lista = [1,2,3,4,5,6,7,8,9,22,55,33,77]

'''print('\nantes: %s\n'%lista)

def inserir(x,v,M):
    #M = 5  # numero maximo de elementos da lista
    if len(v) < M:
        if busca1(x,v):
            v.append(x)
            print('elemento adicionado\n')
        else:
            print('elemento ja existente\n')
    else:
        print('overflow\n')

inserir(25,lista,9)

print('depois: %s'%lista)'''

def remocao(x,v):
    if len(v) == 0:
        print('underflow')
    else:
        encontrado = busca1(x,v)
        if encontrado == -1:
            print('elemento n esta na lista')
        else:
            while encontrado < (len(v)-1):
                v[encontrado] = v[encontrado+1]
                encontrado += 1
    v.pop()
    print(v)


remocao(21,lista)

