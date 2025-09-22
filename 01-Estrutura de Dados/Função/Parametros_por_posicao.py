#o / define que só pode passar por posição, já tendo * e / pode-se usar os dois
def criar_carro(modelo, ano, placa, /, *,marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Pálio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina")
# criar_carro(Modelo="Pálio", ano=1999, placa="ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina")#da erro pois os primeiros parâmetos não aceita com a chave