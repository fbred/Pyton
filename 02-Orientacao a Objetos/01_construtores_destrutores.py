class cachorro:
    def __init__(self, nome, cor, acordado = True): #sempre o construtor inicializador vai ser executado primeiro na instancia da classe
        print("Inicializando a classe")
        self.nome=nome
        self.cor=cor
        self.acordado=acordado

    def lartir(self):
        print("latindo")

    def __del__(self):
        print("Removendo a instancia da classe")

c1 = cachorro("chapie","Caramelo")     

c1.lartir()

