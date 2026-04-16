class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

#Metodo de classe; o mesmo por convenção utiliza o cls
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls (nome, idade)
#Metodo estático de classe;
    @staticmethod
    def e_maio_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 2024, "Antonio")
print(p.nome, p.idade)

print(Pessoa.e_maio_idade(18))
print(Pessoa.e_maio_idade(17))