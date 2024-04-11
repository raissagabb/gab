class Pedido:
    def __init__(self):
        self.itens = {}
        self.total = 0
        self.status = "Pendente"

    def adicionar_item(self, item, preco):
        if item in self.itens:
            self.itens[item] += preco
        else:
            self.itens[item] = preco
        self.total += preco

    def calcular_total(self):
        return self.total

    def alterar_status(self, novo_status):
        self.status = novo_status
pedido = Pedido()
pedido.adicionar_item("Hamburguer", 10)
pedido.adicionar_item("Batata Frita", 5)
pedido.adicionar_item("Refrigerante", 3)
print("Total do pedido:", pedido.calcular_total())
print("Status do pedido:", pedido.status)
pedido.alterar_status("Em preparo")
print("Novo status do  pedido")