class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def emitir_som(self):
        raise NotImplementedError("Método 'emitir_som' deve ser implementado nas subclasses.")

    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Espécie: {self.especie}"


class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"


class Gato(Animal):
    def emitir_som(self):
        return "Miau"


meu_cachorro = Cachorro("Rex", 3, "Cachorro")
print(meu_cachorro.informacoes())
print(meu_cachorro.emitir_som())

meu_gato = Gato("Whiskers", 2, "Gato")
print(meu_gato.informacoes())
print(meu_gato.emitir_som())