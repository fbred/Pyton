frutas = ["laranja", "banana", "uva","carambola","Melão"]
print(frutas)

frutas2=[]
print(frutas2)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

print(frutas[2])
print(frutas[-1])

#lista/matriz 
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "C"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#fatiamento de lista
lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])