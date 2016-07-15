
lista = list(range(11))
lista_len = len(lista)

for i in range(0,lista_len//2):
    temp = lista[i]
    lista[i] = lista[len(lista)-1-i]
    lista[len(lista) - 1 - i] = temp

print(lista)


