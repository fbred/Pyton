class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

# Entrada do usuário
nome = input()
idade = int(input())

# Crie uma instância da pessoa
pessoa = Pessoa(nome, idade)

# Chame o método para retornar as informações formatadas e imprima o resultado
print(pessoa.get_info())