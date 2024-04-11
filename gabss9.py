class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self, media_minima=6):
        media = self.calcular_media()
        if media >= media_minima:
            return f"{self.nome} foi aprovado com média {media:.2f}."
        else:
            return f"{self.nome} foi reprovado com média {media:.2f}."
        
def solicitar_detalhes_estudante():
    nome = input("Insira o nome do estudante: ")
    idade = int(input("Insira a idade do estudante: "))
    notas = []
    continuar = True
    while continuar:
        nota = float(input("Insira uma nota do estudante (ou digite -1 para parar): "))
        if nota == -1:
            continuar = False
        else:
            notas.append(nota)
    return Estudante(nome, idade, notas)

def main():
    estudante = solicitar_detalhes_estudante()
    print(estudante.verificar_aprovacao())

if __name__ == "__main__":
    main()