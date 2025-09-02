nome = "aRaVis"

print(nome.upper()) #deixa todas as letras maiúsculas
print(nome.lower()) #deixa todas as letras minúsculas
print(nome.title()) #deixa a primeira letra de cada palavra maiúscula
print(nome.capitalize()) #deixa a primeira letra da string maiúscula
print(nome.swapcase()) #inverte o caso das letras
print(nome.count("a")) #conta quantas vezes a letra "a" aparece na string
print(nome.find("a")) #retorna o índice da primeira ocorrência da letra "a" 

texto = "  Olá, Mundo!   "

print(texto)
print(texto.strip())  #remove espaços dos dois lados
print(texto.rstrip()) #remove espaços da direita
print(texto.lstrip()) #remove espaços da esquerda

menu = "Python"
print(menu.center(20, "-")) #centraliza a string em um campo de 20 caracteres, preenchendo com "-"
print(menu.ljust(20, "-")) #alinha a string à esquerda em um campo de 20 caracteres, preenchendo com "-"
print(menu.rjust(20, "-")) #alinha a string à direita em um campo de 20 caracteres, preenchendo com "-"
print("-".join(menu)) #faz a iteração colocando o caractere inputado entre os caracteres da string