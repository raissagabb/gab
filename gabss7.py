class Livro:
    def __init__(self,livro,título ,autor ,número_de_páginas):
        self.livro = livro
        self.título = título
        self.autor = autor
        self.número_de_páginas = número_de_páginas
    def contar(self):
        return f"o {self.livro} tem {self.número_de_páginas}  páginas."
    def tema(self):
        return f"o nome do {self.livro} é O Pequeno Principe"
if __name__ == "__main__":
    livro=Livro("pequeno principe ","título","autor","120")
    print(livro.contar())
    print(livro.tema())