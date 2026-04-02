class Cachorro():
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Destruindo a instancia da classe")

    def falar(self):
        print("latindo")

c = Cachorro("Chapie","caramelo")
c.falar()
