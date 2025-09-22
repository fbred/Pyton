#Declarando a função
def exibir_mensagem():
    print(f"Seja bem vindo!!")

def exibir_mensagem2(nome1):
    print(f"Seja bem Vindo: {nome1} !!")

def exibir_mensagem3(nome2="Padrão"):
    print(f"Seja bem vindo: {nome2} !")

#Chamando a função
# exibir_mensagem()
exibir_mensagem2(nome1="teste")
# exibir_mensagem3(nome2="Teste")