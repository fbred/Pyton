# frutas = ["laranja", "banana", "uva","carambola","Melão"]
# print(frutas)

# frutas2=[]
# print(frutas2)

# letras = list("python")
# print(letras)

# numeros = list(range(10))
# print(numeros)

# carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
# print(carro)

# print(frutas[2])
# print(frutas[-1])

# #lista/matriz 
# matriz = [
#     [1, "a", 2],
#     ["b", 3, 4],
#     [6, 5, "C"]
# ]

# print(matriz[0])
# print(matriz[0][0])
# print(matriz[0][-1])
# print(matriz[-1][-1])

# #fatiamento de lista
# lista = ["p", "y", "t", "h", "o", "n"]
# print(lista[2:])
# print(lista[:2])
# print(lista[1:3])
# print(lista[0:3:2])
# print(lista[::])
# print(lista[::-1])

# # ###Usando o for para percorer a lista######
# carros = ["gol","celta","palio"]

# for indice, carro in enumerate(carros):
#     print(f"{indice}: {carro}")


# ###Filtros na lista######
# numeros = [1, 30, 21, 2, 9, 65, 34]
# pares = [numero for numero in numeros if numero % 2 == 0]
# print(pares)

# ####modificando valores####
# numeros2 = [1, 30, 21, 2, 9, 65, 34]
# quadrado = [valor ** 2 for valor in numeros2]
# print(quadrado)
# print(quadrado[0:3])
# print(quadrado[0:1])
# print(quadrado[-1])
# print(quadrado[::-1])

####funções nativas de listas######

#[].copy
lista3 = [1, "python", [2, 5,30, 3], 4.5, True]
lista4 = lista3.copy()
lista5 = lista3[2:4]
print(lista4)
print(lista5)

#[.count]
cores = ["verde", "amarelo", "azul", "branco", "amarelo"]
contador = cores.count("amarelo")
print(f"{contador} vezes o amarelo apareceu na lista")

#[.extend]
linguagens = ["python", "java", "c#"]
outras_linguagens = ["javascript", "php", "c++"]
linguagens.extend(outras_linguagens)
print(linguagens)

#[.index]
lista_nova = ["python", "java", "c#", "php", "c++"]
print(f"o índice de php é {lista_nova.index("php")}")

#[.pop]
linguagens_novo = ["python", "java", "c#", "php", "c++"]
linguagens_novo.pop() # remove o último elemento da lista
print(linguagens_novo)
linguagens_novo.pop(1) # remove o segundo elemento da lista, sendo passado o indice
print(linguagens_novo)

# [.remove]
linguagens_novo.remove("php") # remove o elemento "php" da lista
print(linguagens_novo)

#[.reversed]
print(list(reversed(linguagens_novo))) # inverte a lista

# [.sort]
ordenar_linguagens = ["python", "java", "c#", "php", "c++"]
print(ordenar_linguagens)
ordenar_linguagens.sort()
print(f"Lista ordenada: {ordenar_linguagens}")
ordenar_linguagens.reverse()
print(f"Lista invertida: {ordenar_linguagens}")
ordenar_linguagens.sort(key=lambda x: len(x))
print(f"Lista ordenada pelo tamanho: {ordenar_linguagens}")
ordenar_linguagens.sort(key=lambda x:len(x),reverse=True)
print(f"Lista ordenada pelo tamanho (decrescente): {ordenar_linguagens}")

#[.len]
print(f"O tamanho da lista é: {len(ordenar_linguagens)}")

#[.sorted]
frutas2 = ["laranja", "banana", "uva","carambola","Melão"]
print(f"Lista original: {frutas2}")
print(f"Lista ordenada (sem modificar a original): {sorted(frutas2)}")
sorted_frutas = sorted(frutas2, key=lambda x: x.lower())
print(f"Lista ordenada (sem modificar a original): {sorted_frutas}")