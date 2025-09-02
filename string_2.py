#interpolação de variáveis

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.568

dados = {"nome": "Aravis", "idade": "35"} #Definindo um dicionário

#Metodos menos recomendados de concatenação de variável com string.
print("Nome: %s Idade: %d"%(nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {0} Idade: {1} {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {age}".format(age=idade, name=nome))

print("Nome: {nome}; Idade: {idade}".format(**dados))

#metodo recomendado
print(f"Nome: {nome}; Idade: {idade}; Saldo: {saldo:0.2f}") #Formatando o numero com 0.2f