import functools #com a importação é possível manter o real nome d função

def meu_decorador(funcao):
    @functools.wraps(funcao) #é preciso repassar para poder fucional a chamada da função.
    def envelope(*args, **kwargs):
        funcao(*args, *kwargs)
    return envelope

@meu_decorador 
def ola_mundo(nome):
    print(f"Olá Mundo! {nome}")

print(ola_mundo.__name__)