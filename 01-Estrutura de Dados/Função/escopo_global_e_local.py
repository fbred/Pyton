salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista.append(2)
    lista_aux = lista2.copy()
    lista_aux.append(5)
    print(f"lista auxiliar: {lista_aux}")
    salario += bonus
    return salario

lista = [1]
lista2 = [5]
salario_com_bonus = salario_bonus(500, lista)
print(f"Salário com bônus: {salario_com_bonus}")
print(f"Lista: {lista}")
print(f"lista2: {lista2}")

