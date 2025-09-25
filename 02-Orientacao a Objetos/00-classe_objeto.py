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

    # #método para retornar as instâncias da classe
    # def  __str__(self):
    #     return f"bicicleta: {self.cor, self.modelo, self.ano, self.valor}"

    #método para retornar as instâncias da classe otimizado / Utilizando os atributos que a classe tem como __name__, __dict__, __class__
    # o ', '.join() faz a contaneção do intens da lista com os caracteres que é repassado
    # no f'{chave}={valor} é feito a concatenação dos intens percoridos no laço de repetição for
    # no --> for chave, valor in self.__dict__.items() ->>>  é percorido os itens chave valor através do atributo __dict__ e é armazanado como dicionário
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#instanciamento do objeto
b1 = bicicleta("vermelha", "caloi", 2023, 600)

#acionando os métodos da classe
b1.buzinar()
b1.correr()
b1.parar()

#acessando os atributos da classe
print(b1.cor, b1.ano, b1.modelo, b1.valor)

#criando um segundo objeto
b2 = bicicleta("Azul", "Dois anos", 2025, 251)
print(b2)
