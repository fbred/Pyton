class Estudante:
    escola = "DIO" #variável de classe é unica para cada objeto, se mudar muda em todos os objetos

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula #Variável de objeto varia, e é unica em cada objeto.

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_01 = Estudante("guilherme", 1)
aluno_02 = Estudante("Giovana", 2)
mostrar_valores(aluno_01, aluno_02)

Estudante.escola = "Python"
aluno_03 = Estudante("Chappie", 3)
aluno_01.matricula = 3
mostrar_valores(aluno_01, aluno_02, aluno_03)