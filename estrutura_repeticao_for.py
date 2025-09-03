texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()
    print("Fim do programa") 

#UTILIZANDO O RANGE NO for

# for numero in range(0, 51, 5):
#     print(numero, end=" ")