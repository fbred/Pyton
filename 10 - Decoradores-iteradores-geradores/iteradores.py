#usar o iterador quando a implementação for complexa.

class MeuIterador:
    def __init__(self, numeros: list[int]): #inicializador da classe
        self.numeros = numeros
        self.contador = 0

    def __iter__(self): #iterador (é obrigatório ter)
        return self
    
    def __next__(self): #iterador (é obrigatorio ter se for fazer um iterável)
        try:
            numeros = self.numeros[self.contador]
            self.contador += 1
            return numeros * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)