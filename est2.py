
'''def fat(n):
    if n <= 1:
        return 1
    else:
        return n * fat(n-1)'''

'''fat = 1
for i in range(1,6):
    fat = fat * i
print(fat)'''

lista = [3,9,2,8,5,4,0]

#Busca sequencial

'''Metodo 1

def busca1(x,v):
    i = 0
    while i < len(v):
        if v[i] == x:
            print('valor encontrado na posicao %i'%(i))
            return i
        else:
            i += 1

busca1(0,lista)'''

'''Metodo 2

    def busca2(x,v):
    i = 0
    v.append(x)    #v[len(v) + 1] = x # sentinela
    while v[i] != x:
        i += 1

    if i != (len(v)-1):
        print('tem na posicao ' + str(i))
    else:
        print('nao tem')
busca2(,lista)'''

'''Metodo 3

lista = [3,9,2,8,5,4,0]
lista.sort()

def busca3(x,v):
    i = 0
    lista.append(x)
    while v[i] < x:
        i += 1
    if i < (len(v)-1):
        print('tem')
    else:
        print('n tem')

busca3(9,lista)'''



