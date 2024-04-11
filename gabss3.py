class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {self.saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def mostrar_saldo(self):
        print(f"Saldo atual da conta: {self.saldo}")


minha_conta = ContaBancaria("123456", "Fulano", 1000)
minha_conta.mostrar_saldo()
minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.mostrar_saldo()