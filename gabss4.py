class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def atualizar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        if quantidade > 0:
            print(f"Estoque de {self.nome} atualizado: {self.quantidade_estoque} unidades.")
        elif quantidade < 0:
            print(f"Venda de {self.nome} realizada. Estoque atualizado: {self.quantidade_estoque} unidades.")

    def calcular_preco_total(self, quantidade_desejada):
        if quantidade_desejada <= self.quantidade_estoque:
            preco_total = self.preco * quantidade_desejada
            return preco_total
        else:
            print("Quantidade desejada excede o estoque disponível.")
            return None

produto1 = Produto("Camiseta", 25.0, 50)
print(f"Preço total: R${produto1.calcular_preco_total(5)}")
produto1.atualizar_estoque(-3)
print(f"Preço total: R${produto1.calcular_preco_total(10)}")