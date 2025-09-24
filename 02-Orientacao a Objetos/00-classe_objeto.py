#calsse
class bicicleta:
    #caracteristicas do objeto que a classe define
    def __init__(self, cor, modelo, ano, valor): #inicializador
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor #self é uma referência direta ao atributo, representa a instancia do objeto

    #métodos
    def buzinar(self): #por convenção o método usa self
        print("Buzina acionada, prefiro o silêncio kkkkk!!!")
    
    def parar(self):
        print("Freio acionado...\n")
        print("Bicicleta parada")

    def correr(self):
        print("Bicicleta em movimento...")
    #médor para retornar as instâncias da classe
    def  __str__(self):
        return f"bicicleta: "

#instanciamento do objeto
b1 = bicicleta("vermelha", "caloi", 2023, 600)

#acionando os métodos da classe
b1.buzinar()
b1.correr()
b1.parar()

#acessando os atributos da classe
print(b1.cor, b1.ano, b1.modelo, b1.valor)

#criando um segundo objeto
b2 = bicicleta("Azul", "Dois amor", 2025, 251)

