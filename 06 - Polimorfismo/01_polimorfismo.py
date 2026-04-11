class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voando...")
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

class Aviao:
    def voar(self):
        print("Avião voando...")

# O método plano_voo é polimórfico, pois pode receber objetos de diferentes classes (Pardal e Avestruz)...
#... e chamar o método voar() de cada um, resultando em comportamentos diferentes.
def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())