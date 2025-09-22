def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero +1

    return antecessor, sucessor #retorna o valor em uma tupla

#sem retorno setado tem que retornar NONE, caso for chamada no print
def func_3():
    print("Olá mundo!!")
    
print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3()) #retornar NONE
