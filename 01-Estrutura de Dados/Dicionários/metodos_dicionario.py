##############{}.clear()##############
# O método clear() remove todos os itens de um dicionário.
dicionario = {'a': 1, 'b': 2, 'c': 3}
print("Dicionário original:", dicionario)
dicionario.clear()
print("Dicionário após clear():", dicionario)

##############{}.copy()##############
# O método copy() retorna uma cópia rasa do dicionário.
dicionario_original = {'a': 1, 'b': 2, 'c': 3}
dicionario_copy = dicionario_original.copy()
print("Dicionário original: ", dicionario_original)
print("Cópia do dicionário: ", dicionario_copy)

##############{}.fromkeys()##############
#O metódo cria chaves
print(dict.fromkeys("nome","telefone")) #cria chaves com valor vazio
print(dict.fromkeys(["nome", "telefone"],["vazio"]))#cria chaves com valor atribuido "vazio"


##############{}.get()##############
# O método get() retorna o valor associado a uma chave, ou um valor padrão se a chave não existir.
dicionario = {'a': 1, 'b': 2, 'c': 3}
print("Valor da chave 'a':", dicionario.get('a'))
print("Valor da chave 'd' (não existe):", dicionario.get('d', 'Chave não encontrada')) #é possível passar um segundo argumento caso não enconte a chave indicada
print("valor da chave: C: ", dicionario.get('c'))

##############{}.items()##############
# O método items() retorna uma visão dos pares chave-valor do dicionário.
dicionario = {'a': 1, 'b': 2, 'c': 3}
print("Itens do dicionário:")
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")

##############{}.keys()##############
# O método keys() retorna as chaves do dicionário.
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dicionario.keys())


##############{}.pop()##############
# O método pop() remove e retorna o valor associado a uma chave específica.
dicionario = {'a': 1, 'b': 2, 'c': 3}
valor_removido = dicionario.pop('b')
valor_removido = dicionario.pop('d', 'Chave não encontrada') #caso não encontre a chave indicada retorna o segundo parâmetro
print("Valor removido:", valor_removido)
print("Dicionário após pop():", dicionario)

##############{}.popitem()##############
# O método popitem() remove e retorna o último par chave-valor inserido no dicionário.
dicionario = {'a': 1, 'b': 2, 'c': 3}
chave, valor = dicionario.popitem()
print("Valor removido:", valor)
print("Dicionário após popitem():", dicionario)

##############{}.setdefault()##############
# O método setdefault() retorna o valor de uma chave, se existir. Caso contrário, insere a chave com um valor padrão.
dicionario = {'a': 1, 'b': 2, 'c': 3}
valor = dicionario.setdefault('b', 0) # se o valor default for usado em uma chave que já tem valor ele não substitui, mantem o valor já existente
print("Valor da chave 'b':", valor)
valor = dicionario.setdefault('d', 4) #caso não exista a chave ou o valor, ele faz a atribuição
print("Valor da chave 'd':", valor)
print("Dicionário após setdefault():", dicionario)

##############{}.update()##############
# o método faz atualização do intem que está dentro da chave

contatos = {
    "contato@gmail.com": {"nome": "contato", "telefone": "3333:1111"}
}
print(contatos)

contatos.update({"contato@gmail.com": {"nome": "contatoupdate"}})
print(contatos)

##############{}.values()##############
# o values retorna todos os valores dentro do dicionário.

contatos3 = {
    "contato1": {"nome": "contato1", "telefone": "3333:1111"},
    "contato2": {"nome": "contato2", "telefone": "3333:2222"},
    "contato3": {"nome": "contato3", "telefone": "3333:3333"},
}   
print(contatos3.values())

##############{}.in()##############
# Verificar se uma chave existe em um dicionário

contatos4 = {
    "contato1": {"nome": "contato1", "telefone": "3333:1111"},
    "contato2": {"nome": "contato2", "telefone": "3333:2222"},
    "contato3": {"nome": "contato3", "telefone": "3333:3333"},
}   
retorno = "nome" in contatos4["contato1"]
print(retorno)