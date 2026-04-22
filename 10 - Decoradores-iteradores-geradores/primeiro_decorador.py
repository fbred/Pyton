def meu_decorador(funcao):
    def envelope():
        print('faz algo antes de executar') #pode ser utilizado para fazer uma verificação anterior
        funcao()                            #permite coloca mais de um comportamente em uma função
        print("Faz algo depois de executar")
    return envelope

@meu_decorador #usando arroba na função interna o Python já faz a interpretação, o chamado açucar sintático
def ola_mundo():
    print("Olá Mundo!")

# ola_mundo = meu_decorador(ola_mundo)
ola_mundo()