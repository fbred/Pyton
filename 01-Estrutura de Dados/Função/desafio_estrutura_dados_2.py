# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:

def elementos_comuns(lista1, lista2):  # Define a função que recebe duas listas
    try:
        set1 = set(map(int, lista1))  # Converte lista1 para inteiros e cria um conjunto
        set2 = set(map(int, lista2))  # Converte lista2 para inteiros e cria um conjunto
        return list(set1.intersection(set2))  # Retorna uma lista com os elementos comuns
    except ValueError:
        return "Entrada inválida."  # Retorna mensagem de erro se não for possível converter para inteiro

# Leitura das listas
lista1 = input().split()  # Lê a primeira linha de entrada e separa os valores por espaço
lista2 = input().split()  # Lê a segunda linha de entrada e separa os valores por espaço

# Verifica se todos os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() or (item.startswith('-') and item[1:].isdigit()) for item in lista1) and \
   all(item.isdigit() or (item.startswith('-') and item[1:].isdigit()) for item in lista2):  # Checa se todos os itens são números inteiros (inclusive negativos)
    comuns = elementos_comuns(lista1, lista2)  # Chama a função para encontrar elementos comuns
    print(f"Elementos comuns às duas listas: {comuns}")  # Exibe os elementos comuns
else:
    print("Entrada inválida.")  # Exibe mensagem de erro se houver elemento inválido