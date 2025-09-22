def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro Inserido com sucesso! {marca}, {modelo}, {ano}, {placa}")


salvar_carro("fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"}) #passando o dicionário para a função
