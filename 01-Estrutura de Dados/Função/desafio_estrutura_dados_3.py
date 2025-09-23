def contar_caracteres(string):  # Define uma função que recebe uma string como parâmetro
    # Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.
    contador = {}  # Cria um dicionário vazio para contar os caracteres
    # Itere através de cada caractere na string.
    for caractere in string:  # Percorre cada caractere da string recebida
        # Para cada caractere, verifique se ele já está presente no dicionário contador.
        if caractere in contador:  # Se o caractere já existe como chave no dicionário
            contador[caractere] += 1  # Incrementa o valor associado à chave (quantidade de vezes que apareceu)
        else:
            contador[caractere] = 1  # Se o caractere não existe, adiciona ao dicionário com valor 1
    return contador  # Retorna o dicionário com a contagem de cada caractere

# Solicita entrada do usuário
entrada = input()  # Lê uma string digitada pelo usuário
resultado = contar_caracteres(entrada)  # Chama a função para contar os caracteres da string informada
print(resultado)  # Exibe o dicionário com a contagem de cada caractere