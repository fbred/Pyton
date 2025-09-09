numeros = set([1, 2, 3, 4])
print(numeros)

fruta = set("abacaxi")
print(fruta)

carros = set(("gol", "celta", "uno"))
print(carros)

frutas = {"banana", "laranja", "uva", "banana"} # Duplicados são ignorados
print(frutas)

#########convertendo conjunto em lista#########
frutas = {"banana", "laranja", "uva", "banana"} #declarando um conjunto(set)
frutas_lista = list(frutas)
print(frutas_lista[0]) #imprime o primeiro elemento da lista ->> a função set não tem indexação

###########{}.union()##############
conjuntoa = {1, 2, 3}
conjuntob = {3, 4, 5}
conjuntoc = conjuntoa.union(conjuntob) #une os dois conjuntos, eliminando os duplicados
print(conjuntoc)

###########{}.intersection()##############
conjuntoa = {1, 2, 3}   
conjuntob = {3, 4, 5}
conjuntoc = conjuntoa.intersection(conjuntob) #mostra apenas os elementos que existem em ambos os conjuntos
print(conjuntoc)