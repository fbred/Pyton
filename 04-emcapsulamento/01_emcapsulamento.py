class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # ao atribuir o underline na variável estou indicando que por convenção essa é uma variável privada
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):

        self._saldo += valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta("0001", 100)
print(conta._saldo)
print(conta.mostrar_saldo())
print(conta.nro_agencia)

#O Pyton não tem palavras reservadas para atributos privados do emcapsulamento.