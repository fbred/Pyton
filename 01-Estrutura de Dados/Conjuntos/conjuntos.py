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

###########{}.difference()##############
conjuntoa = {1, 2, 3}
conjuntob = {3, 4, 5}
conjuntoc = conjuntoa.difference(conjuntob) #mostra apenas os elementos que existem no primeiro conjunto e não no segundo
conjuntod = conjuntob.difference(conjuntoa) #mostra apenas os elementos que existem no segundo conjunto e não no primeiro
print(conjuntoc)
print(conjuntod)

###########{}.symmetric_difference()##############
conjuntoa = {1, 2, 3}
conjuntob = {3, 4, 5}
conjuntoc = conjuntoa.symmetric_difference(conjuntob) #mostra apenas os elementos que não existem em ambos os conjuntos
print(conjuntoc)

###########{}.issubset()##############
conjuntoa = {1, 2, 3}
conjuntob = {1, 2, 3, 4, 5}
print(conjuntoa.issubset(conjuntob)) #mostra se o primeiro conjunto é um subconjunto do segundo
print(conjuntob.issubset(conjuntoa)) #mostra se o segundo conjunto é um subconjunto do primeiro

###########{}.issuperset()##############
conjuntoa = {1, 2, 3}
conjuntob = {1, 2}
print(conjuntoa.issuperset(conjuntob)) #mostra se o primeiro conjunto é um superconjunto do segundo
print(conjuntob.issuperset(conjuntoa)) #mostra se o segundo conjunto é um superconjunto do primeiro

###########{}.isdisjoint()##############
conjuntoa = {1, 2, 3}
conjuntob = {4, 5, 6}
conjuntoc = {10,11,2}
print(conjuntoa.isdisjoint(conjuntob)) #mostra se os dois conjuntos não têm elementos em comum
print(conjuntob.isdisjoint(conjuntoa)) #mostra se os dois conjuntos não têm elementos em comum
print(conjuntoc.isdisjoint(conjuntoa)) #mostra se os dois conjuntos não têm elementos em comum
print(conjuntoa.isdisjoint(conjuntob)) #mostra se os dois conjuntos não têm elementos em comum

###########{}.add()##############
conjuntoa = {1, 2, 3}
conjuntoa.add(4) #adiciona o elemento 4 ao conjunto
conjuntoa.add(5) #adiciona o elemento 5 ao conjunto
conjuntoa.add(5) #não adiciona o elemento 5 ao conjunto, pois já existe
print(conjuntoa)

###########{}.clear()##############
conjuntoa = {1, 2, 3}
conjuntoa.clear() #remove todos os elementos do conjunto
print(conjuntoa)

###########{}.copy()##############
conjuntoa = {1, 2, 3}
conjuntoa_copia = conjuntoa.copy() #cria uma cópia do conjunto
print(conjuntoa_copia)

###########{}.discard()##############
conjuntoa = {1, 2, 3}
conjuntoa.discard(2) #remove o elemento 2 do conjunto
print(conjuntoa)
conjuntoa.discard(4) #não faz nada, pois o elemento 4 não está no conjunto
print(conjuntoa)
conjuntoa.remove(3) #remove o elemento 3 do conjunto
print(conjuntoa)