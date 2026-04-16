from abc import ABC, abstractmethod


class ContoleRemoto(ABC):
    @abstractmethod  #método abstrato, não pode ser chamado diretamente
    def ligar(self):
        pass

    @abstractmethod #A classe filha é sempre obrigada a implementar os métodos abstratos
    def desligar():
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ContoleRemoto):
    def ligar(self):
        print("TV ligada")

    def desligar(self):
        print("TV desligada")

    @property
    def marca(self):
        return "LG"

class ControleArcondicionado(ContoleRemoto):
    def ligar(self):
        print("Arcondicionado ligado")

    def desligar(self):
        print("Ar condicionado Desligado")

    @property
    def marca(self):
        return "LG"  

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle2 = ControleArcondicionado()
controle2.ligar()
controle2.desligar()
print(controle2.marca)
