def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('faz algo antes de executar') 
        funcao(*args, **kwargs)                            
        print("Faz algo depois de executar")
    return envelope

@meu_decorador 
def ola_mundo(nome):
    print(f"Olá Mundo! {nome}")

ola_mundo("Jão")